from django.contrib.auth import (
    login as user_login,
)
from django.contrib.auth import (
    logout as user_logout,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import *

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
            return redirect("core:home")
        else:
            print(form.errors)
    else:
        form = SignupForm()
    return render(
        request, "registration/signup.html", {"page_title": "Sign Up", "form": form}
    )


def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            user_login(request, user)
            return redirect("core:home")

        form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()

    return render(
        request,
        "registration/login.html",
        {
            "page_title": "Log In",
            "form": form,
        },
    )


@login_required
def logout_confirm(request):
    return render(
        request, "registration/logout_confirm.html", {"page_title": "Log Out"}
    )


@login_required
def logout(request):
    if request.method == "POST":
        user_logout(request)
        return redirect("core:home")
    else:
        raise ValueError("Can't access logout page through 'get'")


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            user_login(request, request.user)
            return redirect("core:home")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(
        request,
        "registration/change_password.html",
        {"page_title": "Change password", "form": form},
    )


@login_required
def update_profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("core:home")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(
        request,
        "registration/profile_update.html",
        {"page_title": "Edit Profile", "form": form},
    )
