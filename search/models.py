from django.db import models
from blogPost.models import (Blog_Users,Blog_Post)

class searchQuery_QuerySet(models.QuerySet):
	def search_searchQuery(self,query):
		return self.filter(query__icontains = query)

class searchQueryManager(models.Manager):
	def get_queryset(self):
		return searchQuery_QuerySet(self.model, using = self._db)
	def search_searchQuery(self,query = None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search_searchQuery(query)

class searchQuery(models.Model):
	user = models.CharField(max_length = 100)
	query = models.CharField(max_length = 500)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = searchQueryManager()

