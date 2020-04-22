from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name= "dashboard"),
    path('register/', views.register, name= "register_url"),
    path('login/', LoginView.as_view(), name = "login_url"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    path('deactivate/', views.delete_profile, name = "delete_acc" ),
]