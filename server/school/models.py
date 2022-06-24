from django.db import models
class School(models.Model):
    school_name = models.CharField(max_length=300)
    school_address = models.CharField(max_length=250)

# Create your models here.
