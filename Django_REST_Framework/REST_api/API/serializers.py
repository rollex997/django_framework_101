from rest_framework import serializers
from API.models import *

#read a single student record or all student record
class StudentSerializers(serializers.Serializer):
   Student_ID = serializers.IntegerField()
   name=serializers.CharField(max_length=100)
   roll = serializers.IntegerField()
   city=serializers.CharField(max_length=70)
   created_at = serializers.DateTimeField()
   updated_at = serializers.DateTimeField()

#create a new record using DRF 
#this function will allow us to send data from the front end and recieve it in the backend
class StudentSerializers_create(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

# from rest_framework import serializers

# from .models import Student

# class StudentSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['Student_ID', 'name', 'roll', 'city', 'created_at', 'updated_at']