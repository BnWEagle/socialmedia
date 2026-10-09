from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout_confirm/", views.logout_confirm, name="logout_confirm"),
    path("logout/", views.logout, name="logout"),
    path("edit/", views.update_profile, name="update_profile"),
    path("change_password/", views.change_password, name="change_password"),
]