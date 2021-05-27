from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('posts/<str:slug>', posts_detail, name='posts_detail'),
]