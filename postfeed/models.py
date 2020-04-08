from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post", null=True)
    body = models.TextField(max_length=200)
    creation_date = models.DateTimeField(default=now())

    def __str__(self):
        return self.body
