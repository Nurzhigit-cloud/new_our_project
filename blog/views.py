from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
from django.views.generic import DetailView, ListView, DeleteView



def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
class PostListView(ListView):
    model = Post
    template_name = 'blog/post/post_list.html'
    context_object_name = 'post'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
    publish__month=month, publish__day=day)
    return render(request, 'blog/post_detail.html', {'post': post})

class PostDetailsView(DetailView):
    queryset = Post.objects.all()
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'