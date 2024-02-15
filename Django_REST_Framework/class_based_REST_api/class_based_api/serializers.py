from rest_framework import serializers
from class_based_api.models import *
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('ID','name','roll','city')
        read_only_fields = ['ID']