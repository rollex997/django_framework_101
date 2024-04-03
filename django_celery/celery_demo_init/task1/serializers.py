from rest_framework import serializers
from task1.models import *
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name','roll','email','category')

class StudentCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentCategory
        fields = ('id','category')