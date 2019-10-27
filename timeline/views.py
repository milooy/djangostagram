from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from dsuser.models import Dsuser
from django.core.paginator import Paginator
from django.http import Http404


def timeline(request):
    all_posts = Post.objects.all().order_by('-created_date')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_posts, 4)

    posts = paginator.get_page(page)
    return render(request, 'timeline.html', {'posts': posts})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})

def post_upload(request):
    if not request.session.get('user'):
        return redirect('/user/login/')

    print("뭐냐")
    print(request.method)

    if request.method == 'POST':
        print("여기 들어가니")
        form = PostForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            dsuser = Dsuser.objects.get(pk=user_id)

            post = Post()
            post.author = dsuser
            post.image_url = form.cleaned_data['image_url']
            post.text = form.cleaned_data['text']
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'post_upload.html', {'form': form})
