from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from auth_api.models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (['id','username','email','password'])
        read_only_fields = ['id']
    def create(self, validated_data):
        validated_data['is_active'] = False  # Set is_active to False
        user = User.objects.create_user(**validated_data)
        return user
class EmployeeSerializer(serializers.ModelSerializer):
    user  = UserSerializer()
    class Meta:
        model = EmployeeProfile
        fields = ['ID','user','phone','created_on']
        read_only_fileds = ['ID','created_on']
    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extract user data from validated data
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()  # Save the user object
            employee = EmployeeProfile.objects.create(user=user, **validated_data)  # Create employee profile with user
            return employee
        else:
            raise serializers.ValidationError(user_serializer.errors)