from unittest.util import _MAX_LENGTH
from django.db import models
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200)
    teacher_phone = models.PositiveIntegerField(blank=True,null=True)
    teacher_email = models.EmailField(blank=True,null=True)
    teacher_address = models.CharField(max_length=250,blank=True)
class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_phone = models.PositiveIntegerField()
    student_email = models.EmailField()
    student_address = models.CharField(max_length=200)
class Parent(models.Model):
    parents_name = models.CharField(max_length=200)
    parents_phone = models.PositiveBigIntegerField()
    parents_address = models.CharField(max_length=200)
    student_id = models.ForeignKey(Student,on_delete=models.PROTECT)



# Create your models here.
