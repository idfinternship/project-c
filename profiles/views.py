import os

from django.conf import settings
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileEditForm, UserProfileEditForm
from .models import FriendRequest, UserProfile

from django.conf import settings


def profile(request, username):
    current_user = request.user
    searched_user = User.objects.get(username=username)
    sent_friend_requests = FriendRequest.objects.filter(from_user=searched_user)
    rec_friend_requests = FriendRequest.objects.filter(to_user=searched_user)

    searched_user_profile = UserProfile.objects.filter(user=searched_user).first()
    friends = searched_user_profile.friends.all()

    button_status = 'none'
    if searched_user.userprofile not in request.user.userprofile.friends.all():
        button_status = 'not_friend'

        # if sent friend request
        if len(FriendRequest.objects.filter(
                from_user=request.user).filter(to_user=searched_user)) == 1:
            button_status = 'friend_request_sent'
    # end of friend functionality

    context = {
        'searched_user': searched_user,
        'current_user': current_user,
        'button_status': button_status,
        'friend_list': friends,
        'sent_friend_requests': sent_friend_requests,
        'rec_friend_requests': rec_friend_requests,
        'images': gallery(searched_user.username)
    }
    return render(request, 'profile/profile.html', context)


def profile_edit(request):
    if request.method == 'POST':
        user_form = ProfileEditForm(request.POST, instance=request.user)
        profile_form = UserProfileEditForm(request.POST, request.FILES, instance=request.user.userprofile)
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


def friends_view(request, username):
    current_user = request.user
    searched_user = User.objects.get(username=username)
    sent_friend_requests = FriendRequest.objects.filter(from_user=searched_user)
    rec_friend_requests = FriendRequest.objects.filter(to_user=searched_user)
    friends = searched_user.userprofile.friends.all()

    context = {
        'searched_user': searched_user,
        'current_user': current_user,
        'friend_list': friends,
        'sent_friend_requests': sent_friend_requests,
        'rec_friend_requests': rec_friend_requests
    }
    return render(request, 'profile/friends.html', context)


def send_friend_request(request, pk):
    user = get_object_or_404(User, pk=pk)
    frequest, created = FriendRequest.objects.get_or_create(
        from_user=request.user,
        to_user=user
    )

    url = "/profile/" + str(user.username)
    return redirect(url)


def cancel_friend_request(request, pk):
    user = get_object_or_404(User, pk=pk)
    frequest = FriendRequest.objects.filter(
        from_user=request.user,
        to_user=user
    ).first()
    frequest.delete()

    url = "/profile/" + str(user.username)
    return redirect(url)

def cancel_friend_request_from_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    frequest = FriendRequest.objects.filter(
        from_user=request.user,
        to_user=user
    ).first()
    frequest.delete()

    url = "/profile/" + str(request.user.username)
    return redirect(url)


def accept_friend_request(request, pk):
    from_user = get_object_or_404(User, pk=pk)
    frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    user1 = frequest.to_user
    user2 = from_user
    user1.userprofile.friends.add(user2.userprofile)
    user2.userprofile.friends.add(user1.userprofile)
    frequest.delete()

    url = "/profile/" + str(user1.username)
    return redirect(url)


def delete_friend_request(request, pk):
    from_user = get_object_or_404(User, pk=pk)
    frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    frequest.delete()

    url = "/profile/" + str(request.user.username)
    return redirect(url)


def delete_friend(request, username):
    current_user = request.user
    friend_user = User.objects.get(username=username)

    current_user.userprofile.friends.remove(friend_user.userprofile)
    friend_user.userprofile.friends.remove(current_user.userprofile)

    url = "/profile/" + str(friend_user.username)
    return redirect(url)


def gallery(username):
    temp = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    temp += '\profiles\media\photos\{0}'.format(username)
    images = []
    no_files = False
    try:
        path = os.listdir(temp)
    except:
        no_files = True
    if not no_files:
        for image in path:
            images.append("/media/photos/{0}/{1}".format(username, image))
    return images
