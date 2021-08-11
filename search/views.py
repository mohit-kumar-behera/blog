from django.shortcuts import render,get_object_or_404,redirect
from .models import searchQuery
from django.http import HttpResponse,Http404
from django.utils import timezone
import datetime
from blogPost.models import Blog_Post
from blogPost.models import Blog_Users,Blog_Post


def search_query_page_view(request):
	query = request.GET.get('q',None)
	if query is not None:
		query = query.strip()
		if len(query) != 0:
			context = {'query':query}
			
			found_blog_list = Blog_Post.objects.search_blog(query = query).q_post_published().order_by('-date_publish')
			if found_blog_list:
				searchQuery.objects.create(user = request.session['sessUsername'], query = query)
			context['found_blog_list'] = found_blog_list
			present_year = timezone.localtime().year
			num_of_items = len(found_blog_list)
			context['present_year'] = present_year
			context['num_of_items'] = num_of_items

			found_search_list = searchQuery.objects.search_searchQuery(query = query)
			num_of_times_item_searched = len(found_search_list)

			if num_of_times_item_searched >= 10:
				context['search_frequency_text'] = 'Frequently Searched Query'
			elif num_of_times_item_searched < 10:
				context['search_frequency_text'] = 'Less Searched Query'

			context['num_of_times_item_searched'] = num_of_times_item_searched

			return render(request,'search/search_page.html',context)
		elif len(query) == 0:
			return render(request,'search/search_page.html',{'query':'Nothing Searched'})

	elif query is None:
		return redirect('home')


def search_user_profile_view(request):
	if 'view_profile' in request.POST:
		request.session['temp_view_profile_id'] = request.POST.get('view_profile')
		get_user = Blog_Users.objects.get(id = request.session['temp_view_profile_id'])
		get_username = get_user.username
		if get_username == request.session['sessUsername']:
			return redirect('/blogs/profile/',permanent = True)
		else:
			return redirect('viewProfile', permanent = True)




