from __future__ import unicode_literals


# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class ChatGroups(models.Model):
    members = models.ManyToManyField(User, related_name='members')
    name    = models.CharField(max_length = 40)

    def unicode(self):
        return self.name

class Messages(models.Model):
    text_message = models.TextField(default = None)
    timestamp    = models.DateTimeField(default = timezone.localtime(timezone.now()), db_index = True)
    creator      = models.TextField()
    group_obj    = models.ForeignKey(ChatGroups, on_delete= models.CASCADE, related_name = 'messages')

    def __unicode__(self):
        return '[{timestamp}] {creator}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime("%d-%m-%y %H:%M%p")

    def as_dict(self):
        return {'creator': self.creator, 'text_message': self.text_message,'timestamp': self.formatted_timestamp }

