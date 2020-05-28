from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post", null=True)
    body = models.TextField()
    liked = models.ManyToManyField(User, default=None, blank=True, related_name="liked")
    #likes = models.PositiveIntegerField(default=0)
    #users_reaction = models.ManyToManyField(User, blank=True, verbose_name='user_reaction', related_name='react')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    @property
    def num_of_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default="Like", max_length=10)

    def __str__(self):
        return str(self.post)