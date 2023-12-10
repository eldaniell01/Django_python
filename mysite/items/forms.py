from django import forms

from .models import Item

INPUT_CLASSES='form-control'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('id_category', 'name', 'description', 'price', 'image',)
        widgets ={
            'id_category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
            
        }