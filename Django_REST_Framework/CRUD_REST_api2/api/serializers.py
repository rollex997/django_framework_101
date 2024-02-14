from rest_framework import serializers
from api.models import *
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = ['Student_ID','name','roll','city']
        read_only_fields = ['student_ID']
    def validate(self,data):
        name=data.get('name')
        roll=data.get('roll')
        if roll==997 or name.lower()=='rollex':
            raise serializers.ValidationError('Rollex cannot be added')
        elif roll>200:
            raise serializers.ValidationError('Seats full')
        else:
            return data