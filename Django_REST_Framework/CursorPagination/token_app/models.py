from django.db import models
# Create your models here.
# to create token using signal
class Student(models.Model):
    ID=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    city=models.CharField(max_length=70)
    # created=models.DateTimeField(auto_now_add=True)
