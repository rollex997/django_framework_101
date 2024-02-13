from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from API.serializers import *
from API.models import *
import io
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
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

#create : create a record after recieveing data from the front end
@csrf_exempt
def create_student(request):
    if request.method=='POST':
        json_data = request.body  #getting the reuqest body because the method is POST
        stream = io.BytesIO(json_data) # convert the request body into json_data
        python_data=JSONParser().parse(stream) # convert json_data into python data
        serializer = StudentSerializers_create(data=python_data) # conver python  data into complex data 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':'data created'})
        else:
            print(serializer.errors)
            return JsonResponse({'status':serializer.errors})
        
@csrf_exempt
def update_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        # Get the student instance to update
        student_id = int(python_data.get('Student_ID'))
        print(student_id)
        try:
            student_instance = Student.objects.get(Student_ID=student_id)

            # Update the instance with the new data
            student_instance.Student_ID=python_data.get('Student_ID')
            student_instance.name=python_data.get('name')
            student_instance.roll=python_data.get('roll')
            student_instance.city=python_data.get('city')
            student_instance.save()
            return JsonResponse({'status': 200})
        except Student.DoesNotExist:
            return JsonResponse({'status': 'Error', 'message': 'Student does not exist'}, status=404)
        
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from .models import Student
# import io

# @csrf_exempt
# def update_student(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
        
#         # Get the student instance to update
#         student_id = int(python_data.get('Student_ID'))
#         try:
#             student_instance = Student.objects.get(Student_ID=student_id)
            
#             # Update the instance with the new data
#             for key, value in python_data.items():
#                 setattr(student_instance, key, value)
#             student_instance.save()
            
#             return JsonResponse({'status': 200})
        
#         except Student.DoesNotExist:
#             return JsonResponse({'status': 'Error', 'message': 'Student does not exist'}, status=404)
