from django import forms
from .models import ConversationMessage

INPUT_CLASSES = 'form-control'

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            })
        }