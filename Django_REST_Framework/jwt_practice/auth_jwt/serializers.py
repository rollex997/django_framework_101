from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from auth_jwt.models import * 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','username','email','password']
        read_only_fields = ['id',]
        def create(self,validated_data):
            # validated_data['is_active']=False
            user = User.objects.create_user(**validated_data)
            return user
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'role','role_name']
        read_only_fields = ['id',]

class UserRoleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id','role_list']
        read_only_fields = ['id',]
    
