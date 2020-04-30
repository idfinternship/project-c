from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import profile

app_name = 'profiles'
urlpatterns = [
    #path('', views.profile, name='profile'), old profile view
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/change_password/', views.change_password, name='change_password'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/search_results/', views.user_search, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
