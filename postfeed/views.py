from django.shortcuts import render, redirect, get_object_or_404
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

        return redirect('postfeed:posts', username=request.user.username)

    return render(request, 'postfeed/create.html', context={'form': form})

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('postfeed:posts', username=request.user.username)

@login_required
def posts(request, username):
    searched_user = User.objects.get(username=username)
    posts = searched_user.post.all().order_by('-creation_date')

    return render(request, 'postfeed/posts.html', context={'searched_user': searched_user, 'posts': posts})

