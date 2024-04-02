from rest_framework import serializers
from marks.models import *
from task1.models import *
from task1.serializers import *
class MarksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ('id', 'student', 'maths', 'physics', 'chemistry', 'english', 'hindi')

    def create(self, validated_data):
        student_id = validated_data.pop('student')
        student = Student.objects.get(id=student_id)
        marks = Marks.objects.create(student=student, **validated_data)
        return marks

class Get_All_MarksSerializers(serializers.ModelSerializer):
    #Nested serializers for related student model
    student = StudentSerializers()
    class Meta:
        model = Marks
        fields = ('id', 'student', 'maths', 'physics', 'chemistry', 'english', 'hindi')
            