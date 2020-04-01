from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
from .forms import PostCreateForm

from . import views

# Create your views here.
def index(response):
    return HttpResponse("postfeed index response")

def detail(request):
    pass

def create(request):
    form = PostCreateForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'postfeed/create.html', context={'form': form})

def posts(request):
    post_list = Post.objects.all()

    return render(request, 'postfeed/posts.html', context={'post_list': post_list})