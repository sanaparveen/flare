from django.conf.urls import url
from flare import views
from flare.classviews import GroupsListView, GroupsCreateView, GroupsDetailView, GroupsUpdateView, GroupsDeleteView
from flare.views import chat

urlpatterns = [

    url(r'^$', views.welcome, name='index'),
    url(r'^home/$',GroupsListView.as_view(), name = 'homepage'),
    url(r'^groups/$', GroupsListView.as_view(), name = 'groups_list'),
    url(r'^groups/new/$', GroupsCreateView.as_view(), name = 'groups_create'),
    url(r'^groups/(?P<pk>[0-9]+)/chat/$',chat,name = 'groups_chat'),
    url(r'^groups/(?P<pk>[0-9]+)/update/$',  GroupsUpdateView.as_view(), name = 'groups_update'),
    url(r'^groups/(?P<pk>[0-9]+)/delete/$',  GroupsDeleteView.as_view(), name = 'groups_delete'),
    url(r'^groups/(?P<pk>[0-9]+)/members/$', GroupsDetailView.as_view(), name = 'groups_details')
]
