#coding: utf-8
from django.conf.urls import patterns, url, include
from dj_project.views import *
from haystack.views import SearchView


urlpatterns = patterns('',
    url(r'^$', WeaponsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', WeaponDetailView.as_view()),  # а по URL http://имя_сайта/cw/число/
    url(r'^([0-9]+?)/(?P<pk>\d+)/$', ModelWeaponDetailView.as_view()),
    url(r'^([0-9]+?)/(p)/(?P<pk>\d+)/$', PatronDetailView.as_view()),
    url(r'^search/', include('haystack.urls')),
    url(r'^report/', PatronListView.as_view()),

    url(r'^dj_project/$', 'django.views.static.serve',
        {'document_root': '/home/god/work/Coursework/dj_project/templates/dj_project'}),
    )
