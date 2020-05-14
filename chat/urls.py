from django.urls import path, re_path

from .views import ThreadView, InboxView, friends_view_inbox

app_name = 'chat'
urlpatterns = [
    path("", friends_view_inbox, name='inbox'),
    re_path(r"^(?P<username>[\w.@+-]+)/$", ThreadView.as_view(), name='thread'),
]
