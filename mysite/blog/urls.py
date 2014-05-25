from django.conf.urls import patterns, include, url
from django.views.generic import ListView,DetailView
from mysite.blog.models import Post
from mysite.blog.views import TagBlogView,BlogView,ArchiveBlogView
urlpatterns = patterns('',
	 url(r'^$',BlogView.as_view()),
	 url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name="post.html")),
	 url(r'^tag/(?P<tag>.*)$',TagBlogView.as_view()),
	 url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})$',ArchiveBlogView.as_view()),
)
