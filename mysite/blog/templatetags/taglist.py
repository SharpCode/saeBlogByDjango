from django import template
from mysite.blog.models import Post
from taggit.models import Tag
register=template.Library()

@register.inclusion_tag("taglist.html")
def taglist():
	tags=Tag.objects.all()
	return {'tags':tags}
