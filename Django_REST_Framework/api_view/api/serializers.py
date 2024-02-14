from rest_framework import serializers
from api.models import *
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = ['Student_ID','name','roll','city']
        read_only_fields=['Student_ID']