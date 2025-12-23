from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import EmailAuthenticationForm, SignUpForm


def index(request):
    return render(request, "retail/index.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()

    return render(request, "retail/signup.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "retail/login.html"
    authentication_form = EmailAuthenticationForm
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = "/"


@login_required
def home(request):
    return render(request, "retail/home.html")
