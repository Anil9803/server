from django.db import models
from user.models import Student
from subject.models import Subject
class Exam(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.PROTECT)
    subject_id = models.ForeignKey(Subject,on_delete=models.PROTECT)
    exam_date =models.DateField()



# Create your models here.
