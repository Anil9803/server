from django.db import models
class Result(models.Model):
    result_name = models.CharField(max_length=100)
    result_content = models.CharField(max_length=250)
    teacher_comments = models.TextField()

# Create your models here.
