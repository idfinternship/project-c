from django.urls import path

from . import views

app_name = 'postfeed'
urlpatterns = [
    path('profile/<username>/posts', views.posts, name='posts'),
    path('create/', views.create, name='create'),
    path('delete_post/<pk>', views.delete_post, name='delete_post'),
]