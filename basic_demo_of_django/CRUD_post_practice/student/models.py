from django.db import models

# Create your models here.
class Student(models.Model):
    student_ID = models.BigAutoField(primary_key=True)
    student_name = models.CharField(max_length = 70)
    roll_no = models.IntegerField(null=True)
    mobile = models.BigIntegerField(null=True)
    father_name = models.CharField(max_length = 70)
    mother_name = models.CharField(max_length = 70)
    father_mobile = models.BigIntegerField(null=True)