
from django.urls import path,include
from .import views

urlpatterns = [
    path('search/',views.search_query_page_view,name="search"),
    path('sv_profile/',views.search_user_profile_view,name="svProfile")
]
