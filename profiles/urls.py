from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/change_password/', views.change_password, name='change_password'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/search_results/', views.user_search, name='search'),
    path('friend-request/send/<pk>', views.send_friend_request, name='send_friend_request'),
    path('friend-request/cancel/<pk>', views.cancel_friend_request, name='cancel_friend_request'),
    path('friend-request/accept/<pk>', views.accept_friend_request, name='accept_friend_request'),
    path('friend-request/delete/<pk>', views.delete_friend_request, name='delete_friend_request'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
