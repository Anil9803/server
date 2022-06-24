from django.db import models
from user.models import Student
class Homework(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.PROTECT)
    assigned_date = models.DateField()
    homework_details = models.TextField()
    due_date = models.DateField()
    Grade = models.CharField(max_length=5)
# Create your models here.
