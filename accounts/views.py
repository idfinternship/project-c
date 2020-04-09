from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def indexView(request):
    return render(request,'registration/index.html')

@login_required
def dashboardView(request):
    return render(request,'registration/dashboard.html')
def registerView(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = RegistrationForm()

    return render(request,'registration/register.html', {'form':form})
