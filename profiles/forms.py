from django.contrib.auth.forms import UserChangeForm, forms
from django.contrib.auth.models import User
from profiles.models import UserProfile


class ProfileEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'age',
            'gender',
            'icon',
        )