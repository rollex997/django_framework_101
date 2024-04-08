from django.db import models

# Create your models here.
class StudentCategory(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField(unique=True)
    email=models.EmailField(max_length=125)
    category=models.ManyToManyField(StudentCategory)
    def __str__(self):
        return self.name