from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.shortcuts import redirect, render

from .forms import *


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
            return redirect("core:home")

    form = SignupForm()
    return render(
        request, "registration/signup.html", {"page_title": "Sign Up", "form": form}
    )


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=request.POST["username"],
                password=request.POST["password"],
            )
            if user is not None:
                user_login(request, user)
                return redirect("core:home")
                
 
    form = LoginForm()
    return render(request, "registration/login.html", {
        "page_title": "Log In", "form": form,
    })

def logout_confirm(request):
    return render(request, "registration/logout_confirm.html", {
        "page_title": "Log Out", 
    })
