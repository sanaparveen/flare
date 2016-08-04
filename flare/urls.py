from django.conf.urls import url
from flare import views
from flare.classviews import GroupListView, GroupCreateView, GroupDetailView, GroupUpdateView, GroupDeleteView
from flare.views import chat

urlpatterns = [

    url(r'^$', views.welcome, name='index'),
    url(r'^home/$',GroupListView.as_view(), name = 'homepage'),
    url(r'^groups/$', GroupListView.as_view(), name = 'groups_list'),
    url(r'^groups/add/$', GroupCreateView.as_view(), name = 'groups_create'),
    url(r'^groups/(?P<pk>[0-9]+)/chat/$',chat,name = 'groups_chat'),
    url(r'^groups/(?P<pk>[0-9]+)/members/$', GroupDetailView.as_view(), name = 'details'),
    url(r'^groups/(?P<pk>[0-9]+)/update/$',  GroupUpdateView.as_view(), name = 'update'),
    url(r'^groups/(?P<pk>[0-9]+)/delete/$',  GroupDeleteView.as_view(), name = 'delete'),
]
