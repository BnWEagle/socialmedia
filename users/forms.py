from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailInput()
    username = forms.CharField(
        max_length=50,
        min_length=10,
    )
    password1 = forms.CharField(
        max_length=50,
        min_length=10,
        widget = forms.PasswordInput(),
    )
    password2 = forms.CharField(
        max_length=50,
        min_length=10,
        widget = forms.PasswordInput(),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=50,
        min_length=10,
    )
    password1 = forms.CharField(
        max_length=50,
        min_length=10,
        widget = forms.PasswordInput(),
    )
    password2 = forms.CharField(
        max_length=50,
        min_length=10,
        widget = forms.PasswordInput(),
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]