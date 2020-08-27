from django.contrib import admin
from .models import (Blog_Users,Blog_Post)


class Blog_Users_View(admin.ModelAdmin):
	list_display = ('username','password','date_joined')

class Blog_Post_View(admin.ModelAdmin):
	list_display = ('user','blog_title','date_created','date_publish')

admin.site.register(Blog_Users,Blog_Users_View)
admin.site.register(Blog_Post,Blog_Post_View)
