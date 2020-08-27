
from django.urls import path
from . import views

urlpatterns = [
	path('',views.blog_create_log_view,name="base"),
    path('home/',views.blog_home_page_view,name="home"),
    path('view_profile/',views.blog_view_profile_page_view,name='viewProfile')
    
]
