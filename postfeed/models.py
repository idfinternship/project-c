from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post", null=True)
    body = models.TextField(max_length=200)
    likes = models.PositiveIntegerField(default=0)
    users_reaction = models.ManyToManyField(User, blank=True, verbose_name='user_reaction', related_name='react')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
