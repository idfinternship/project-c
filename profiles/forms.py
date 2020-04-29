from django.contrib.auth.forms import UserChangeForm, forms
from django.contrib.auth.models import User



class ProfileEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )