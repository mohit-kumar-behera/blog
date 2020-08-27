from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from blogPost.models import (Blog_Users,Blog_Post)
from django.utils import timezone
from django.urls import reverse
import datetime
from blogPost.models import (Blog_Users,Blog_Post)
from .forms import (Blog_edit_Form,Blog_post_Form)

def blog_uProfile_page_view(request):
	try:
		user = request.session['sessUsername']
		pwd = request.session['sessPassword']
	except:
		return redirect("base")
	else:
		get_blog_user = Blog_Users.objects.get(username = request.session['sessUsername'], password = request.session['sessPassword'])
		get_user_id = get_blog_user.id
		get_user_joined_date = get_blog_user.date_joined

		blog_list_published = Blog_Post.objects.filter(user = get_user_id,date_publish__lte = timezone.localtime()).order_by("-date_publish")

		blog_list_pending = Blog_Post.objects.filter(user = get_user_id,date_publish__gt = timezone.localtime()).order_by("date_publish")
		
		if 'log_out' in request.POST:
			del request.session['sessUsername']
			del request.session['sessPassword']
			return redirect("base")

		if 'blog_delete' in request.POST:
			delete_blog_id = request.POST.get('blog_post_id')
			get_blog = get_object_or_404(Blog_Post,id = delete_blog_id)
			get_blog.delete()

		if 'edit_blog' in request.POST:
			edit_blog_id = request.POST.get('edit_blog')
			request.session['temp_edit_blog_id'] = edit_blog_id
			return redirect('edit_Blog',permanent = True)
			
			
		context = {'blog_list_published':blog_list_published,'blog_list_pending':blog_list_pending,'blog_username':request.session['sessUsername'],'date_joined':get_user_joined_date,'present_year':timezone.localtime().year}
		return render(request,'blogPost/blog_uProfile.html',context)

def blog_edit_page_view(request):
	try:
		request.session['temp_edit_blog_id']
	except:
		return redirect('uProfile')
	else:
		get_blog = get_object_or_404(Blog_Post,id = request.session['temp_edit_blog_id'])
		form = Blog_edit_Form(request.POST or None, request.FILES or None, instance = get_blog)
		if form.is_valid():
			form.save()
			del request.session['temp_edit_blog_id']
			return redirect("uProfile",permanent = True)
		context = {'form':form,'title':f'Update : {get_blog.blog_title}','present_year':timezone.localtime().year} 
		return render(request,'blogPost/blog_edit.html',context)


def blog_post_page_view(request):
	form = Blog_post_Form(request.POST or None, request.FILES or None)
	get_blog_user = Blog_Users.objects.get(username = request.session['sessUsername'],password = request.session['sessPassword'])
	
	if request.POST:
		if form.is_valid():
			get_date_publish = form.cleaned_data.get("date_publish")
			get_blog_title = form.cleaned_data.get("blog_title")
			get_blog_text = form.cleaned_data.get("blog_text")
			get_blog_image = form.cleaned_data.get("blog_image")
			if get_date_publish < timezone.localtime():
				get_date_publish = timezone.localtime() + datetime.timedelta(seconds = 0)
			get_blog_user.blog_post_set.create(blog_title = get_blog_title, blog_text = get_blog_text, blog_image = get_blog_image, date_publish = get_date_publish)
			
			return redirect('uProfile',permanent = True)


	context = {"form":form,"title":"POST BLOG",'present_year':timezone.localtime().year}
	return render(request,'blogPost/blog_post.html',context) 




