
from django.urls import path,include
from .import views

urlpatterns = [
    path('profile/',views.blog_uProfile_page_view,name="uProfile"),
    path('profile/blog_post/',views.blog_post_page_view,name="postBlog"),
   # path('view_profile/<int:get_user_id>/',views.blog_vProfile_page_view,name='vProfile')
    path('profile/edit_blog',views.blog_edit_page_view,name='edit_Blog')
]
