from django import template
from mysite.blog.models import Post
from taggit.models import Tag
from django.db import connection
from django.db.models import Count


register=template.Library()

@register.inclusion_tag("archivelist.html")
def archivelist():
	truncate_date=connection.ops.date_trunc_sql('month','created')
	qs=Post.objects.extra({'time':truncate_date})
	archives=qs.values('time').annotate(count=Count('pk'))
	return {'archives':archives}
