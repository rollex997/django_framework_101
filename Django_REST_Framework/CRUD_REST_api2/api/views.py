from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import io
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from api.models import *
from api.serializers import *
@csrf_exempt
def create_student(request):
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializers(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':'create data success!!!'})
        else:
            return JsonResponse({'status':serializer.errors})
@csrf_exempt
def update_student(request):
    if request.method=='POST':
        json_data = request.body
        stream=io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        try:
            student = Student.objects.get(Student_ID = python_data['Student_ID'])
            serializer = StudentSerializers(student,data=python_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'status':'student updated successfully'})
        except Student.DoesNotExist:
            return JsonResponse({'status':'student does not exist'})
@csrf_exempt
def get_all_student(request):
    if request.method=='POST':
        student=Student.objects.all()
        serializer = StudentSerializers(student,many=True)
        return JsonResponse({'data':serializer.data})
@csrf_exempt
def get_one_student(request):
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        try:
           student = Student.objects.get(Student_ID=python_data['Student_ID'])
           serializers = StudentSerializers(student)
           return JsonResponse({'data':serializers.data})
        except Student.DoesNotExist:
            return JsonResponse({'status':'student does not exist'})
@csrf_exempt
def delete_student(request):
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        try:
            student= Student.objects.get(Student_ID=python_data['Student_ID'])
            student.delete()
            return JsonResponse({'status':'Student deleted successfully!!!'})
        except Student.DoesNotExist:
            return JsonResponse({'status':'student does not exist'}) 