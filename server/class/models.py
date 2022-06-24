from unicodedata import name
from django.db import models
from user.models import Student
from user.models import Teacher
class Class(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.ForeignKey(Student, on_delete=models.PROTECT)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.PROTECT)






# Create your models here.
