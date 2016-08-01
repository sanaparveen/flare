from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from flare.forms import GroupCreationUpdationForm
from flare.models import *

class UserProfileView(DetailView):
    model = User

    def get_queryset(self):
        return self.request.user
    pass
class GroupListView(ListView):
    model = ChatGroups

    def get_queryset(self):
        id = self.request.user.id
        return ChatGroups.objects.filter(members__id__in = [id])

    pass

class GroupCreateView(CreateView):
    model = ChatGroups
    #fields = ['members', 'name']
    form_class = GroupCreationUpdationForm

    def get_success_url(self):
        return reverse('groups_list')
    pass

class GroupDetailView(DetailView):
    model = ChatGroups
    pass

class GroupUpdateView(UpdateView):
    model = ChatGroups
    form_class = GroupCreationUpdationForm

    def get_success_url(self):
        return reverse('groups_list')
    pass

class GroupDeleteView(DeleteView):
    model = ChatGroups

    def get_success_url(self):
        return reverse('groups_list')
    pass



