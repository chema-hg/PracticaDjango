from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserCreationWithEmailForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico', required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

