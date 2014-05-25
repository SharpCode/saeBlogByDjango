from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
     url(r'^$',include('mysite.blog.urls')),
     url(r'^admin/', include(admin.site.urls)),
	 url(r'^blog/',include('mysite.blog.urls')),
	 url(r'^ueditor/',include('mysite.ueditor.urls')),

#	 url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':'static/'}),
#	 url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':'static/'}),
#	 url(r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':'static'}),
#	 url(r'^blog/(?P<path>.*)$','django.views.static.serve',{'document_root':'blog/templates/'}),
	 
	 
)

