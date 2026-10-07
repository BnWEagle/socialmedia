from django.contrib.auth import (
    login as user_login,
    logout as user_logout,
)
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
        
    return render(request, "registration/login.html", {
        "page_title": "Log In", "form": form,
    })

def logout_confirm(request):
    return render(request, "registration/logout_confirm.html", {"page_title": "Log Out"})
    
def logout(request):
    if request.method == "POST":
        user_logout(request)     
        return redirect("core:home")
    else:
        raise ValueError("Can't access logout page through 'get'")

