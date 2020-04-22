from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileEditForm
# Create your views here.


 #def profile(request):
 #   args = {'searched_user': request.user}
 #   return render(request, 'profile/profile.html', args)

def profile(request, username):
    current_user = request.user
    searched_user = User.objects.get(username=username)
    args = {'searched_user': searched_user, 'current_user': current_user}
    return render(request, 'profile/profile.html', args)

def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = ProfileEditForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profile/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:
            return redirect('profile/change/password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'profile/change_password.html', args)


