from django.contrib import admin
from  .models import searchQuery


class searchQueryAdmin(admin.ModelAdmin):
	list_display = ('user','query','timestamp')
	list_filter = ['user']

admin.site.register(searchQuery,searchQueryAdmin)
