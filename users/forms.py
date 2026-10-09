from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

from .models import UserProfile


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    user_name = forms.CharField(
        max_length=50,
        min_length=2,
    )
    first_name = forms.CharField(
        max_length=50,
        min_length=2,
    )
    last_name = forms.CharField(
        max_length=50,
        min_length=2,
    )
    about = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3}),
    )
    profile_picture = forms.ImageField(
        required=False,
    )
    

    class Meta:
        model = UserProfile
        fields = (
            "user_name",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "about",
            "profile_picture",
        )


class ProfileUpdateForm(UserChangeForm):
    user_name = forms.CharField(
        max_length=50,
        min_length=2,
    )
    first_name = forms.CharField(
        max_length=50,
        min_length=2,
    )
    last_name = forms.CharField(
        max_length=50,
        min_length=2,
    )
    about = forms.CharField(
        required = False,
        widget = forms.Textarea(attrs={'rows': 3}),
    )
    password = None
    
    class Meta:
        model = UserProfile
        fields = ( 'user_name', 'first_name', 'last_name', 'about', 'profile_picture' )

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email", 
        widget=forms.EmailInput(),
    )
