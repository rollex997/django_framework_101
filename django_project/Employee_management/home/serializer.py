from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from home.models import EmployeeExperience

class EmployeeExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model=EmployeeExperience
        fields=['ID','company_name','role','date_of_joining','last_date']
        read_only_fields=['ID',]