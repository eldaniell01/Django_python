from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control",
        'id': "floatingInput"
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':"form-control",
        'id': "floatingPassword"
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':"form-control",
        'id': "floatingPassword"
    }))
    
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control",
        'id': "floatingInput",
        'name': "username"
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':"form-control",
        'id': "floatingPassword",
        'name': "password"
    }))