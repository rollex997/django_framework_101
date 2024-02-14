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
    '''field level validation'''
    # def validate_roll(self,value):
    #     if value>=200:
    #         raise serializers.ValidationError("Seats full")
    #     else:
    #         return value
    '''object level validation'''
    # def validate(self,data):
    #     name = data.get('name')
    #     roll = data.get('roll')
    #     if roll == 997 or name.lower() == 'rollex':
    #         raise serializers.ValidationError('Rollex cannot be added')
    #     else:
    #         return data