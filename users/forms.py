from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile


class SignupForm(UserCreationForm):
    email = forms.EmailInput()
    user_name = forms.CharField(
        max_length=50,
        min_length=10,
    )
    first_name = forms.CharField(
        max_length=150,
        min_length=10,
    )
    last_name = forms.CharField(
        max_length=150,
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
    profile_picture = forms.ImageField(
        required=False
    )

    class Meta:
        model = UserProfile
        fields = ( "user_name", "first_name", "last_name", "email", "password1", "password2", "profile_picture" )

class LoginForm(AuthenticationForm):
    email = forms.CharField(
        max_length=50,
        min_length=10,
    )
    password1 = forms.CharField(
        max_length=50,
        min_length=10,
        widget = forms.PasswordInput(),
    )

    class Meta:
        model = UserProfile
        fields = ( "email", "password1" )