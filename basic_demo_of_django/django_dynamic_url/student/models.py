from ctypes import BigEndianStructure
from django.db import models

# Create your models here.
class Student(models.Model):
    student_ID = models.BigAutoField(primary_key=True,blank=True)
    Student_Name = models.CharField(max_length = 70,blank=True)
    Father_Name = models.CharField(max_length = 70,blank=True)
    roll_no = models.IntegerField(blank=True)
    mobile = models.BigIntegerField(blank=True)
    email = models.EmailField(blank=True)
    