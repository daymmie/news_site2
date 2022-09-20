from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-post_date'
    template_name = 'news.html'
    context_object_name = 'post_list'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail_view.html'
    context_object_name = 'post_detail'
