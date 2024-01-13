from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, EmailField

# Create your models here.
class Student(models.Model):
    StID = models.BigAutoField(primary_key=True)
    student_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length = 70)
    comment = models.CharField(max_length=40,default='not available')