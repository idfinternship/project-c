from django.shortcuts import render
# Create your views here.


def profile(request):
    args = {'user': request.user}
    return render(request, 'profile/profile.html', args)
