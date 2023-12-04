from django import forms
from .models import Students


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['student_number', 'first_name', 'last_name', 'email', 'curse', 'gpa']
        labels ={
            'student_number': 'Número de Estudiante',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
            'curse': 'Curso',
            'gpa': 'GPA'
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}), 
            'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'curse': forms.TextInput(attrs={'class': 'form-control'}), 
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}), 
        }