from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from viewSet.models import *
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = ['ID','name','roll','city']
        read_only_fields = ['ID']