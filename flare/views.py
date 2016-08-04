

# Create your views here.
from datetime import time
from webbrowser import get
import time
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from flare.forms import RegistrationForm

from flare.models import Messages, ChatGroups
from django.contrib.auth.models import User

def welcome(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('groups_list'))
    else:
        return render_to_response('flare/index.html')

def welcome1(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('groups_list'))
    else:
        return render_to_response('flare/index.html')

def homepage(request):
    if request.user.is_authenticated():
        return render_to_response('flare/homepage.html', {'user': request.user,})
    else:
        return HttpResponseRedirect('/accounts/login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('../../accounts/login/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'register.html',
        variables,
    )

def chat(request, pk):
    group_obj = ChatGroups.objects.get(id=pk)
    messages = reversed(group_obj.messages.order_by('-timestamp')[:50])
    return render(request, "flare/ChatGroups_chat.html", {'group': group_obj,
                        'messages': messages, })

