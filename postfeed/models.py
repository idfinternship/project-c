from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE) need user authorization to do this
    body = models.TextField(max_length=200)
    creation_date = models.DateTimeField(default=now())
