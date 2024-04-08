from rest_framework import serializers
from task1.models import *
class StudentSerializers(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=StudentCategory.objects.all(), many=True)
    class Meta:
        model = Student
        fields = ('id','name','roll','email','category')

class StudentCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentCategory
        fields = ('id','category')

class GetAllStudentSerializers(serializers.ModelSerializer):
    #because category is a ManyToManyField
    category = StudentCategorySerializers(many=True)
    class Meta:
        model = Student
        fields = ('id','name','roll','email','category')