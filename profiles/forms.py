from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class ProfileEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
        )
