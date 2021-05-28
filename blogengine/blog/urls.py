from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('posts/<str:slug>', posts_detail, name='posts_detail'),
    path('tags/', tags_list, name='tags_list'),
    path('tags/<str:slug>', tags_detail, name='tags_detail'),
]