from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("home/", views.home, name="home"),
    path("store-visits/", views.store_visit_list, name="store_visit_list"),
    path(
        "store-visits/create/",
        views.create_store_visit,
        name="store_visit_create",
    ),
    path(
        "store-visits/<int:store_visit_id>/",
        views.store_visit_detail,
        name="store_visit_detail",
    ),
]
