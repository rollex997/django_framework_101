from decimal import MAX_EMAX
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Student(models.Model):
    SID = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 70)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.SID} - {self.name}"