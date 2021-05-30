from django.shortcuts import render, redirect
from django.views.generic import View

from .models import *
from .utils import *
from .forms import *


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html',
                  context={'posts': posts})  # ключи словаря контекст, будут использованы в шаблоне


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectsCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectsCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
