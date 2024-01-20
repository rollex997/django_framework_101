from django.db import models

# Create your models here.
class Student_info(models.Model):
    student_ID = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 70)
    roll_no = models.CharField(max_length = 200)
    mobile = models.CharField(max_length = 10)
    father_name = models.CharField(max_length = 70)
    mother_name = models.CharField(max_length = 70)
    father_mobile = models.CharField(max_length = 70)