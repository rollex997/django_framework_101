from email.policy import default
from django.db import models
from student.models import *
# Create your models here.
class Marks(models.Model):
    marks_ID = models.BigAutoField(primary_key=True)
    Student_ID = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='marks')
    Student_name = models.CharField(max_length=70)
    Maths = models.FloatField()
    Physics = models.FloatField()
    Chemistry = models.FloatField()
    Computer = models.FloatField()
    English = models.FloatField()
    Hindi = models.FloatField()
    Total_marks_obtained = models.FloatField()
    Percentage = models.FloatField()
    pass_fail = models.BooleanField()
class MarksSettings(models.Model):
    marks_settings_ID = models.IntegerField(default=1)
    passing_percentage = models.FloatField(default = 40)
    passing_marks_per_subject = models.FloatField(default=40)
    Total_marks_per_subject = models.FloatField()