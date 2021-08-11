from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .forms import (Create_UserForm,Login_UserForm)
from .models import (Blog_Users,Blog_Post)
from django import forms
from django.utils import timezone
import datetime

def blog_create_log_view(request):
	try:
		user = request.session['sessUsername']
		password = request.session['sessPassword']
	except:
		form1 = Create_UserForm()
		form2 = Login_UserForm()
		if 'c_submit' in request.POST:
			form1 = Create_UserForm(request.POST or None)
			if form1.is_valid():
				form1.save()
				form1 = Create_UserForm()

		else:
			form2 = Login_UserForm(request.POST or None)
			if form2.is_valid():
				username = form2.cleaned_data.get('username')
				password = form2.cleaned_data.get('password')
				query_set1 = Blog_Users.objects.filter(username = username,password = password)
				if query_set1.exists():
					request.session['sessUsername'] = username
					request.session['sessPassword'] = password
					return redirect("home")
				else:
					error_message = 'Account Doesn\'t Exist\nCreate a new one!'
					context = {'form1':form1,'form2':form2,'error_message':error_message}
					return render(request,'blogPost/createAndLogin.html',context)
				form2 = Login_UserForm()	
	else:		
		return redirect("home")
		
	context = {'form1':form1,'form2':form2}
	return render(request,'blogPost/createAndLogin.html',context)

def blog_home_page_view(request):
	try:
		user = request.session['sessUsername']
		pwd =  request.session['sessPassword']
	except:
		return redirect("base")
	else:
		if request.session['sessUsername'] and request.session['sessPassword']:
			try:
				time_now = timezone.localtime()

				#blog_list = Blog_Post.objects.filter(date_publish__lte = time_now).order_by('-date_publish')
				''' The above one was default one '''

				blog_list = Blog_Post.objects.q_post_published().order_by('-date_publish')
				''' The above one was with help of MODAL MANAGER only which is a better option '''

				#blog_pending_list = Blog_Post.objects.filter(date_publish__gt = time_now).order_by('date_publish')
				''' The above one was default one '''
				blog_pending_list = Blog_Post.objects.q_post_pending().all()
				''' The above one was with help of MODAL MANAGER only which is a better option '''

			except Blog_Users.DoesNotExist:
				raise Http404
			else:
				if 'view_profile' in request.POST:
					request.session['temp_view_profile_id'] = request.POST.get('view_profile')
					get_user = Blog_Users.objects.get(id = request.session['temp_view_profile_id'])
					get_username = get_user.username
					if get_username == request.session['sessUsername']:
						return redirect('/blogs/profile/',permanent = True)
					else:
						return redirect('viewProfile', permanent = True)

				context = {'blog_list':blog_list,'blog_pending_list':blog_pending_list,'year':timezone.localtime().year} 
				return render(request,'blogPost/blogs.html',context)
		else:
			return redirect("base")


def blog_view_profile_page_view(request):
	try:
		get_blog_user = request.session['temp_view_profile_id']
	except:
		return redirect('base')
	else:
		get_blog_user = Blog_Users.objects.get(id = request.session['temp_view_profile_id'])
		get_view_user_joined_date = get_blog_user.date_joined
		get_view_username = get_blog_user.username
		get_view_user_id = request.session['temp_view_profile_id']
		blog_list_published = Blog_Post.objects.filter(user = get_view_user_id,date_publish__lte = timezone.localtime()).order_by("-date_publish")
		blog_list_pending = Blog_Post.objects.filter(user = get_view_user_id,date_publish__gt = timezone.localtime()).order_by("date_publish")
		context = {'blog_list_published':blog_list_published,'blog_list_pending':blog_list_pending,'blog_view_username':get_view_username,'date_joined':get_view_user_joined_date,'present_year':timezone.localtime().year}
		return render(request,'blogPost/blog_vProfile.html',context)


