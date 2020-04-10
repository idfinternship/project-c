from accounts.forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def index(request):

@login_required
def dashboard(request):

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = RegistrationForm()

