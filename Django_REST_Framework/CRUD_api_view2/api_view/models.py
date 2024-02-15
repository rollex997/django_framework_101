from django.db import models
class Student(models.Model):
    ID=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=70)
    roll=models.IntegerField()
    city=models.CharField(max_length=70)