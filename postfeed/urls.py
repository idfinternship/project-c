from django.urls import path

from . import views

app_name = 'postfeed'
urlpatterns = [
    #path('<int:post_id>/', views.posts, name='posts'),
    path('', views.posts, name='posts'),
    path('create/', views.create, name='create'),
]