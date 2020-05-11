from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
from django.dispatch import receiver


def upload_path(instance, filename):
    return 'photos/{0}/{1}'.format(instance.user.username, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=25, null=True, blank=True, default="")
    icon = models.ImageField(upload_to=upload_path, blank=True, null=True, default='photos/default.jpg')
    gallery = models.ImageField(upload_to=upload_path, blank=True, null=True)
    friends = models.ManyToManyField("UserProfile", blank=True)

    def __str__(self):
        return self.user.username


class FriendRequest(models.Model):
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
