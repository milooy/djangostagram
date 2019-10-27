from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def timeline(request):
    posts = Post.objects.all().order_by('created_date')
    return render(request, 'timeline.html', {'posts': posts})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})

def post_upload(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            dsuser = Dsuser.objects.get(pk=user_id)

            post = Post()
            post.author = dsuser
            post.image_url = form.cleaned_data['image_url']
            post.text = form.cleaned_data['text']
            post.created_date = timezone.now()
            post.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_upload.html', {'form': form})
