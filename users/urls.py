from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout_confirm/", views.logout_confirm, name="logout_confirm"),
    path("logout/", views.user_logout, name="logout"),
    path("edit/", views.update_profile, name="update_profile"),
    path("change_password/", views.change_password, name="change_password"),
    path("delete_profile/", views.delete_profile, name="delete_profile"),
]