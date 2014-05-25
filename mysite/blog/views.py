# Create your views here.
from django.views.generic import ListView
from mysite.blog.models import Post

class BlogView(ListView):
	paginate_by=5
	template_name="blog.html"
	
	def get_queryset(self):
		return Post.objects.all().order_by('-created')

class TagBlogView(BlogView):

	def get_queryset(self):
		tag=self.kwargs['tag']
		return Post.objects.filter(tags__name=tag).order_by('-created')

class ArchiveBlogView(BlogView):
	
	def get_queryset(self):
		year=self.kwargs['year']
		month=self.kwargs['month']
		return Post.objects.filter(created__year=year,created__month=month).order_by('-created')
