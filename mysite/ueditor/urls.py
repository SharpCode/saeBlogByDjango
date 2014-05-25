from django.conf.urls import patterns, include, url
from mysite.ueditor.views import controller
urlpatterns = patterns('',
	url(r'^config.*$',controller),
)
