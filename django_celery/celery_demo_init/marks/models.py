from django.db import models
from task1.models import *
# Create your models here.
class Marks(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    maths = models.FloatField()
    physics = models.FloatField()
    chemistry = models.FloatField()
    english = models.FloatField()
    hindi = models.FloatField()