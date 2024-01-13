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
    #this is to make our data Human readable in admin panel 
    #after registering this model in admin application
    def __str__(self):
        #This will show the ID and name of the student in the list
        return f"{self.SID} - {self.name}"