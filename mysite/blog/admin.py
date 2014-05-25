from django.contrib import admin
from mysite.blog.models import Post

class PostAdmin(admin.ModelAdmin):
	class Media:
		js={
			'/static/js/ueditor/extra.js',
			'/static/js/ueditor/ueditor.config.js',
			'/static/js/ueditor/ueditor.all.min.js',
		}

admin.site.register(Post,PostAdmin)
