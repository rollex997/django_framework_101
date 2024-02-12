from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from API.serializers import *
from API.models import *
# Model Object: get a single Student data from a database
def student_detail(request,Student_ID):
    student = Student.objects.get(Student_ID=Student_ID) # complex data or model object
    print(student)
    serializer = StudentSerializers(student) # python data or python dictionary
    print(serializer.data)
    return JsonResponse({'data':serializer.data})
#query set: get all student data from a model
def student_list(request):
    student = Student.objects.all()
    print(student)
    serializer=StudentSerializers(student,many=True)
    print(serializer.data)
    return JsonResponse({'data':serializer.data})