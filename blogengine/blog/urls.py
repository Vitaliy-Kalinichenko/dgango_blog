from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('posts/<str:slug>', PostDetail.as_view(), name='posts_detail'),
    path('tags/', tags_list, name='tags_list'),
    path('tags/<str:slug>', TagDetail.as_view(), name='tags_detail'),
]
