from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name= "dashboard"),
    path('register/', views.register, name= "register_url"),
    path('login/', LoginView.as_view(), name = "login_url"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    path('deactivate/', views.delete_profile, name = "delete_acc" ),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name = "password_reset" ),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done' ),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm' ),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_complete.html"), name = "password_reset_complete" ),
]