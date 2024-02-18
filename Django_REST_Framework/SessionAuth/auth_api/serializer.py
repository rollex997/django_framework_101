# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from auth_api.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['ID','name','roll','city']
        read_only_fields=['ID']