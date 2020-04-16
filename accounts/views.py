from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.decorators import login_required


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

