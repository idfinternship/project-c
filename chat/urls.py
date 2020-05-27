from django.urls import path, re_path

from .views import ThreadView, friends_view, friends_view1

app_name = 'chat'
urlpatterns = [
    path("", friends_view, name='inbox'),
    re_path(r"^(?P<username>[\w.@+-]+)/$", ThreadView.as_view(), name='thread'),
    re_path("1", friends_view1, name='friendslists'),
]
