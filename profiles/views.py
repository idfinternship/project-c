from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileEditForm, UserProfileEditForm


def profile(request, username):
    current_user = request.user
    searched_user = User.objects.get(username=username)
    args = {'searched_user': searched_user, 'current_user': current_user}
    return render(request, 'profile/profile.html', args)


def profile_edit(request):
    if request.method == 'POST':
        user_form = ProfileEditForm(request.POST, instance=request.user)
        profile_form = UserProfileEditForm(request.POST, request.FILES,  instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            url = "/profile/" + str(request.user.username)
            return redirect(url)
    else:
        user_form = ProfileEditForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.userprofile)
        args = {'form': user_form, 'profile_form': profile_form}
        return render(request, 'profile/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            url = "/profile/" + str(request.user.username)
            return redirect(url)
        else:
            return redirect('profile/change/password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'profile/change_password.html', args)


def user_search(request):
    query = request.GET.get('q')
    if not query:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    users = User.objects.filter(Q(username__icontains=query))

    if not users:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'profile/search_results.html', {'users': users})

