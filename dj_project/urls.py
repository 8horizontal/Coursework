#coding: utf-8
from django.conf.urls import patterns, url
from dj_project.views import PostsListView, PostDetailView


urlpatterns = patterns('',
    url(r'^$', PostsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # а по URL http://имя_сайта/blog/число/
                                                      # будет выводиться пост с определенным номером
    )
