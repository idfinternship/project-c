from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post
from .forms import PostCreateForm

from . import views

def index(response):
    return HttpResponse("postfeed index response")

def detail(request):
    pass

def create(request):
    form = PostCreateForm(request.POST or None)

    if form.is_valid():
        body = form.cleaned_data["body"]
        post = Post(body=body)
        post.save()
        request.user.post.add(post)

        return redirect('postfeed:posts')

    return render(request, 'postfeed/create.html', context={'form': form})

def posts(request):
    post_list = Post.objects.all()

    return render(request, 'postfeed/posts.html', context={'post_list': post_list})