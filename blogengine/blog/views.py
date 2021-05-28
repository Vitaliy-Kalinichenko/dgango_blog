from django.shortcuts import render

from .models import *


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html',
                  context={'posts': posts})  # ключи словаря контекст, будут использованы в шаблоне


def posts_detail(request, slug):  # slug - то что приходит из urlpatterns
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/posts_detail.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def tags_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tags_detail.html', context={'tag': tag})
