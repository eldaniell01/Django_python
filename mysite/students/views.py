from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Students
from .forms import StudentForm


# Create your views here.
def index(request):
    return render(request, 'students/students.html', {
        'students': Students.objects.all()
    })
    
def view_student(request, id):
    student = Students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_curse = form.cleaned_data['curse']
            new_gpa = form.cleaned_data['gpa']
            
            new_student = Students(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                curse = new_curse,
                gpa = new_gpa
            )
            
            new_student.save()
            return render(request, 'students/add_student.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
            form = StudentForm()
    return render(request, 'students/add_student.html', {
        'form': StudentForm()
    })
    

def edit_student(request, id):
    if request.method=='POST':
        student = Students.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Students.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })
    
def delete(request, id):
    if request.method == 'POST':
        student = Students.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect(reverse('index'))