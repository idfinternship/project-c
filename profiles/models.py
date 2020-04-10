from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
# Create your models here.


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_day = models.DateField(blank=True, default='')
    currently_living_in = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=20)


# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
#
# def delete(sender, **kwargs):
#     delete_profile = kwargs['instance']
#     delete_profile.username.delete()
#
#
# post_save.connect(create_profile, sender=User)
# post_delete.connect(delete, sender=UserProfile)
