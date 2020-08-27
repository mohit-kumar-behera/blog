from django.db import models
from django.utils import timezone
from django.db.models import Q

''' Use of only modal manager '''
class BlogPostModelManager(models.Manager):
	def m_post_published(self):
		return self.get_queryset().filter(date_publish__lte = timezone.localtime())
	def m_post_pending(self):
		return self.get_queryset().filter(date_publish__gt = timezone.localtime())
''' End of modal manager '''



''' Using Modal Manager and Query_Set Together to do the above function in better way '''
class BlogPostQuerySet(models.QuerySet):
	def q_post_published(self):
		return self.filter(date_publish__lte = timezone.localtime())
	def q_post_pending(self):
		return self.filter(date_publish__gt = timezone.localtime())
	def search_blog(self,query):
		lookup = (
					Q(blog_title__icontains = query) |
					Q(blog_text__icontains = query) |
					Q(date_publish__icontains = query)
					#Q(user__icontains = query)
				)
		#return self.filter(blog_title__icontains = query)
		return self.filter(lookup)

class BlogPostQueryModalManager(models.Manager):
	def get_queryset(self):
		return BlogPostQuerySet(self.model, using = self._db)
	def q_post_published(self):
		return self.get_queryset().q_post_published()
	def q_post_pending(self):
		return self.get_queryset().q_post_pending()
	def search_blog(self,query = None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search_blog(query)

'''End of Modal Manger and QuerySet '''

class Blog_Users(models.Model):
	username = models.CharField(max_length = 35, unique = True)
	password = models.CharField(max_length = 30)
	date_joined = models.DateTimeField(auto_now_add = True)
	def __str__(self,*args,**kwargs):
		return self.username	

	
class Blog_Post(models.Model):
	user = models.ForeignKey(Blog_Users,on_delete = models.CASCADE)
	blog_title = models.CharField(max_length = 100)
	blog_text = models.TextField()
	blog_image = models.ImageField(upload_to = 'image/',blank = True)
	date_created = models.DateTimeField(auto_now_add = True)
	date_publish = models.DateTimeField(auto_now_add = False)

	objects = BlogPostModelManager()
	objects = BlogPostQueryModalManager()

	def __str__(self):
		return self.blog_text