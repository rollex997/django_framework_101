from django.db import models

# Create your models here.
class EmployeeExperience(models.Model):
    ID=models.BigAutoField(primary_key=True)
    company_name=models.CharField(max_length=100)
    role=models.CharField(max_length=70)
    date_of_joining=models.DateField()
    last_date=models.DateField()