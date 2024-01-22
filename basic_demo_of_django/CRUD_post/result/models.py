from django.db import models
from student.models import *
# Create your models here.
class marks(models.Model):
    marks_ID = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Student_info,null=False,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=70)
    science = models.FloatField()
    math = models.FloatField()
    computerScience = models.FloatField()
    Total_marks_per_subject = models.FloatField()
    Total_obtained_marks = models.FloatField()
    percentage = models.FloatField()
    passingPercentage = models.FloatField()
    pass_fail = models.BooleanField(default=False)