from django.contrib import admin
from django.urls import path
from . import views

from .views import BlogsView,SingleView,PostCreate,UpdatePost

urlpatterns = [
    path('post/',PostCreate.as_view(),name="post-create"),
    path('update/<slug:slug>/',UpdatePost.as_view() ,name="update-post"),

    # path('<slug:slug>/',views.single_post,name="single-post"),
    path('',BlogsView.as_view(),name='home'),
    path('<slug:slug>/',SingleView.as_view(),name="single-post"),
   
]
