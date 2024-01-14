from django.db import models

# Create your models here.
class Student(models.Model):
    SID = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 70)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=70)
    roll_number = models.IntegerField()