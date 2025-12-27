from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmailAuthenticationForm, SignUpForm
from .models import PriceTag, Receipt, StoreVisit


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


@login_required
def create_store_visit(request):
    if request.method != "POST":
        return redirect("store_visit_list")

    store_visit = StoreVisit.objects.create(user=request.user)
    return redirect("store_visit_detail", store_visit_id=store_visit.id)


@login_required
def store_visit_list(request):
    store_visits = (
        StoreVisit.objects.filter(user=request.user)
        .annotate(pricetag_count=Count("pricetag"))
        .order_by("-created_at")
    )
    return render(
        request,
        "retail/store_visit_list.html",
        {"store_visits": store_visits},
    )


@login_required
def store_visit_detail(request, store_visit_id):
    store_visit = get_object_or_404(
        StoreVisit,
        id=store_visit_id,
        user=request.user,
    )
    pricetags = PriceTag.objects.filter(store_visit=store_visit).order_by(
        "-created_at"
    )
    receipts = Receipt.objects.filter(store_visit=store_visit).order_by(
        "-created_at"
    )
    return render(
        request,
        "retail/store_visit_detail.html",
        {
            "store_visit": store_visit,
            "pricetags": pricetags,
            "receipts": receipts,
        },
    )
