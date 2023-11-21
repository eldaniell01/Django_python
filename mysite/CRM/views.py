from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SingUpForm, addCustomer
from .models import ModelCustomers
# Create your views here.


def home(request):
    """revisa si esta logeado """
    customers = ModelCustomers.objects.all()
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
        return render(request, 'crm/home.html', {'customer':customers})

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

def customer(request, pk):
    if request.user.is_authenticated:
        customer = ModelCustomers.objects.get(id=pk)
        return render(request, 'crm/customer.html',{'customer': customer})
    else:
        messages.success(request, 'debes de estar logeado para ver esta página')
        return redirect('home')
    
def delete_customer(request, pk):
    if request.user.is_authenticated:
        customer = ModelCustomers.objects.get(id=pk)
        customer.delete()
        messages.success(request, 'se ha eliminado cliente')
        return redirect('home')
    else:
        messages.success(request, 'debes de estar logeado para ver esta página')
        return redirect('home')
    
def add_customer(request):
    form = addCustomer(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_customer = form.save()
                messages.success(request, 'cliente registrado')
                return redirect('home')
        return render(request, 'crm/add_customer.html', {'form': form})
    else:
        messages.success(request, 'debes de estar logeado para ver esta página')
        return redirect('home')
    
def update_customer(request, pk):
    if request.user.is_authenticated:
        customer = ModelCustomers.objects.get(id=pk)
        form = addCustomer(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'cliente actualizado')
            return redirect('home')
        return render(request, 'crm/update_customer.html', {'form': form})
    else:
        messages.success(request, 'debes de estar logeado para ver esta página')
        return redirect('home')
