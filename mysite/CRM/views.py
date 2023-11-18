from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SingUpForm
# Create your views here.


def home(request):
    """revisa si esta logeado """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'estas logeado')
            return redirect('home')
        else: 
            messages.success(request, 'error al iniciar sesión')
            return redirect('home')
    else:
        return render(request, 'crm/home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'has cerrado sesión')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'registro completo')
            return redirect('home')
    else:
        form = SingUpForm()   
    
        return render(request, 'crm/register.html', {'form': form})
    return render(request, 'crm/register.html', {'form': form})