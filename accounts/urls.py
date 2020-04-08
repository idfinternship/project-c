<<<<<<< HEAD
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexView, name="home"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('register/', views.registerView, name="register_url"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name="logout"),
=======
from django.urls import  path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.indexView,name= "home"),
    path('dashboard/',views.dashboardView,name ="dashboard"),
    path('register/',views.registerView,name="register_url"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name= "logout"),
>>>>>>> ef59fdf0afdd0725cd4ca6f75261fc936f782838
]