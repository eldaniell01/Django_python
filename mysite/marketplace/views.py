from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from items.models import Category, Item
from .forms import SignUpForm
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:10]
    categories = Category.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('marketplace:index')
    else:
        return render(request, 'marketplace/products.html',{
            'categories': categories,
            'items': items
        })

def contact(request):
    return render(request, 'marketplace/contact.html')

def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marketplace:login')
    else:
       form=SignUpForm()
    return render(request, 'marketplace/signup.html',{
        'form':form
    })

def logout_user(request):
    logout(request)
    return redirect('marketplace:index')