
from django.urls import path,include
from .import views

app_name = 'blogProfile'

urlpatterns = [
    path('profile/',views.blog_uProfile_page_view,name="uProfile"),
    path('view/profile/',views.blog_view_profile_page_view,name='vProfile'),
    path('profile/blog_post/',views.blog_post_page_view,name="postBlog"),
    path('edit_blog/',views.blog_edit_page_view,name='edit_Blog')
]
