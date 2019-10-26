from django.shortcuts import render, get_object_or_404
from .models import Post


def timeline(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'timeline.html', {'posts': posts})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})