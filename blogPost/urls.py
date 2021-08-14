
from django.urls import path
from . import views

urlpatterns = [
	path('',views.blog_create_log_view,name="base"),
    path('blogs/',views.blog_home_page_view,name="home")
]
