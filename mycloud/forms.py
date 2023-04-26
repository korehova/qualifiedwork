from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'input-box'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input-box'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'input-box'}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'input-box'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input-box'}))

