from django.contrib.auth import login, logout


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import *

# Create your views here.

def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("core:home")
        else:
            print(form.errors)
    else:
        form = SignupForm()
    return render(
        request, "registration/signup.html", {"page_title": "Sign Up", "form": form}
    )


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("core:home")

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
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("core:home")
    else:
        raise ValueError("Can't access logout page through 'get'")


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            login(request, request.user)
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


@login_required
def delete_profile(request):
    user = request.user
    if request.method == "POST":
        UserProfile.objects.get(id=user.id).delete()
        return redirect("core:home")

    return render(
        request, "registration/delete_account.html", {"page_title": "Delete Account"}
    )
