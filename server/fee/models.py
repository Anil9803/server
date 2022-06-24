from django.db import models
from user.models import Student
student_id = models.ForeignKey(Student, on_delete=models.PROTECT)
fee_paid = models.DecimalField(10,2)
fee_due = models.DecimalField(10,2)



# Create your models here.
