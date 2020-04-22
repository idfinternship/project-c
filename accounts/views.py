from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import  logout


def index(request):
    return render(request, 'accounts/index.html')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login_url')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

def delete_profile(request):
    user = request.user
    user.is_active = False
    user.save()
    logout(request)
    return redirect('accounts:login_url')

