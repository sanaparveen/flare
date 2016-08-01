import re
import json
import logging
from channels import Group
from channels.sessions import channel_session

from flare.models import ChatGroups

log = logging.getLogger(__name__)

@channel_session
def ws_connect(message):

    try:
        [prefix, group_id] = message['path'].decode('ascii').strip('/').split('/')[1:3]
        if prefix != 'groups':
            log.debug('invalid ws path = %s', message['path'])
            return
        group = ChatGroups.objects.get(id = group_id)
    except ValueError:
        log.debug('invalid ws path = %s', message['path'])
        return
    except ChatGroups.DoesNotExist:
        log.debug('ws room does not exist group_id = %s', group_id)
        return
    Group('chat-'+group_id, channel_layer = message.channel_layer).add(message.reply_channel)
    message.channel_session['group'] = group_id


@channel_session
def ws_receive(message):

    try:
        group_id = message.channel_session['group']
        group = ChatGroups.objects.get(id=group_id)
    except KeyError:
        log.debug('no room in channel_session')
        return
    except ChatGroups.DoesNotExist:
        log.debug('received message, buy room does not exist group_id=%s',group_id)
        return

    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", data)
        return

    if set(data.keys()) != set(('creator', 'text_message')):
        log.debug("ws message unexpected format data = %s", data)
        return
    if data:
        log.debug('chat message room= %s handle = %s message= %s',
                  group.name, data['creator'], data['text_message'])
        m = group.messages.create(**data)

        Group('chat-'+group_id, channel_layer = message.channel_layer).send({'text': json.dumps(m.as_dict())})


@channel_session
def ws_disconnect(message):
    try:
        group_id = message.channel_session['group']
        group = ChatGroups.objects.get(id = group_id)
        Group('chat-'+group_id, channel_layer = message.channel_layer).discard(message.reply_channel)
    except (KeyError, ChatGroups.DoesNotExist):
        pass

