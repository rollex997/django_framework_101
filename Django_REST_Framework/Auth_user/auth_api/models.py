from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EmployeeProfile(models.Model):
    ID = models.BigAutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    created_on=models.DateField(auto_now_add=True)
    