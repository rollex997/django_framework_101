from django.db import models

# Create your models here.
class Student(models.Model):
    Student_ID = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    roll = models.IntegerField()
    city=models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)