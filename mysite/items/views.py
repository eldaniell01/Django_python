from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import NewItemForm
# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(id_category=item.id_category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })
    
@login_required 
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            if item.image:
                return redirect('item:detail', pk=item.id)
            else:
                return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm
    return render(request, 'item/form.html',{
        'form': form
    })
    
@login_required
def delete(request, pk):
    if request.method=='POST':
        item = Item.objects.get(pk=pk)
        item.delete()
        return redirect('dashboard:index')