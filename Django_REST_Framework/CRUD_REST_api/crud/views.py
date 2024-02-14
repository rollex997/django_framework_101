from django.shortcuts import render
from crud.models import *
from django.views.decorators.csrf import csrf_exempt
import io
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from crud.serializers import *

#get all student records from DB
@csrf_exempt
def get_all_student(request):
    if request.method=='POST':
        student = Student.objects.all()
        serializer = StudentSerializers(student,many=True)
        return JsonResponse({'data':serializer.data}) 

#get a single student record 
@csrf_exempt
def student_detail(request):
    if request.method=='POST':
        json_data = request.body
        stream=io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        student_id = python_data['Student_ID']
        try:
            student=Student.objects.get(Student_ID=student_id)
            serializer = StudentSerializers(student)
            return JsonResponse({'data':serializer.data})
        except Student.DoesNotExist:
            return JsonResponse({'status':'student detail not found'})

# Create a student record
@csrf_exempt
def create_student(request):
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        print(python_data)
        serializers = StudentSerializers_create(data=python_data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse({'status':'create student success'})
        else:
            return JsonResponse({'status':serializers.errors})

# Update your student record (complete and partial update supported)
@csrf_exempt
def update_student(request):
    if request.method=='POST':
        json_data = request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        try:
            student_id = python_data['Student_ID']
            student = Student.objects.get(Student_ID = student_id)
            student.Student_ID = python_data['Student_ID']
            # Update only the fields that are provided in the request data
            # Update fields provided in the request data
            for field in ['name', 'roll', 'city']:
                if field in python_data:
                    setattr(student, field, python_data[field])
            student.save()
            return JsonResponse({'status':'Student record updated'})
        except Student.DoesNotExist:
            return JsonResponse({'status':'Student does not exist'})

@csrf_exempt
def delete_student(request):
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        try:
            student = Student.objects.get(Student_ID=python_data['Student_ID'])
            student.delete()
            return JsonResponse({'status':'Student delete operation successfull'})
        except Student.DoesNotExist:
            return JsonResponse({'status':'Student does not exist'})