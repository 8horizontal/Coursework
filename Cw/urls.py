from django.conf.urls import patterns, include, url
from dj_project.views import *
from django.contrib import admin
from haystack.views import SearchView


admin.autodiscover()
urlpatterns = patterns('',
    url(r'^cw/', include('dj_project.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
