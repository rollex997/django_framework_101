from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from mixin_api.models import *
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['ID','name','roll','city']
        read_only_fields=['ID']