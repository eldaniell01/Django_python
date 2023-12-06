from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'marketplace/products.html')

def contact(request):
    return render(request, 'marketplace/contact.html')