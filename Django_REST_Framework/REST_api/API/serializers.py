from rest_framework import serializers

from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['Student_ID', 'name', 'roll', 'city', 'created_at', 'updated_at']
        read_only_fields = ['Student_ID']