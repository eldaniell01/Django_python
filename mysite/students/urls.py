from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:id>', views.view_student, name='view_student'),
    path('register/', views.add_student, name='add'),
    path('edit/<int:id>', views.edit_student, name='edit'),
    path('delete/<int:id>', views.delete, name='delete')
]
