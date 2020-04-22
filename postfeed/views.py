from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostCreateForm

from . import views
@login_required
def create(request):
    form = PostCreateForm(request.POST or None)

    if form.is_valid():
        body = form.cleaned_data["body"]
        post = Post(body=body)
        post.save()
        request.user.post.add(post)

        return redirect('postfeed:posts')

    return render(request, 'postfeed/create.html', context={'form': form})

@login_required
def posts(request, username):
    user = User.objects.get(username=username)
    posts = user.post.all()

    return render(request, 'postfeed/posts.html', context={'user': user, 'posts': posts})