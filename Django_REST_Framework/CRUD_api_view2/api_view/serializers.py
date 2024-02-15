from rest_framework import serializers
from api_view.models import *
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = ('ID','name','roll','city')
        read_only_fields = ['ID']
    def validate(self,data):
        roll=data.get('roll')
        if roll>=1000:
            raise serializers.ValidationError('Seats full')
        else:
           return data 