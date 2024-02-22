from django.db import models
# Create your models here.
# to create token using signal
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
class Student(models.Model):
    ID=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    city=models.CharField(max_length=70)
    passby = models.CharField(max_length=70)
