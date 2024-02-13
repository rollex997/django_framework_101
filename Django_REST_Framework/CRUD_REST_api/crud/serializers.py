from rest_framework import serializers
from crud.models import *

class StudentSerializers(serializers.Serializer):
    Student_ID = serializers.IntegerField()
    name = serializers.CharField(max_length=70)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

#create data in the DB
class StudentSerializers_create(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['Student_ID','name','roll','city']