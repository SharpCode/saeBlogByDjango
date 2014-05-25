#coding:utf8
from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
	title=models.CharField('标题',max_length=100)
	body=models.TextField('正文')
	created=models.DateTimeField('创建时间')
	tags=TaggableManager('标签')
	
	@classmethod
	def taglist(cls):
		return "hello world"

	def __unicode__(self):
		return self.title
	
	class Meta:
		verbose_name='博文'
		verbose_name_plural='博文'
		



