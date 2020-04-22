from django.urls import path

from . import views
from .views import profile

app_name = 'profiles'
urlpatterns = [
    #path('', views.profile, name='profile'), old profile view
    path('edit/', views.profile_edit, name='profile_edit'),
    path('change_password/', views.change_password, name='change_password'),
    path('<username>', views.profile, name='profile')

]
