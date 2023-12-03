from django.db import models

# Create your models here.
class Students(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    curse = models.CharField(max_length=50)
    gpa = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f'{self.student_number} {self.first_name} {self.last_name}')
    