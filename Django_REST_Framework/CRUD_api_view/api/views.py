from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models import *
from api.serializers import *
# Create your views here.
@api_view(['POST','PUT'])
def create_update_student(request):
    if request.method=='PUT':
        Student_ID = request.data.get('Student_ID')
        print(Student_ID)
        if Student_ID:
            try:
                student = Student.objects.get(Student_ID = Student_ID)
                serializer = StudentSerializers(student, data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status':'data updated'},status=200)
                else:
                    return Response({'status':serializer.errors},status=400)
            except Student.DoesNotExist:
                return Response({'status':'student does not exist'},status=404)
    if request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'data created successfully!!'},status=200)
        else:
            return Response({'status':serializer.errors},status=400)
@api_view(['GET','POST'])
def get_one_all_student(request):
    if request.method=='GET':
            student=Student.objects.all()
            serializer=StudentSerializers(student,many=True)
            return Response({'data':serializer.data})
    if request.method=='POST':
        Student_ID = request.data.get('Student_ID')
        if Student_ID:
            try:
                student = Student.objects.get(Student_ID=Student_ID)
                serializer = StudentSerializers(student)
                return Response({'data':serializer.data})
            except Student.DoesNotExist:
                return Response({'status':'student does not exist'},status=404)
        else:
            return Response({'status':'Student_ID not present'})
@api_view(['POST'])
def delete_student(request):
    if request.method=='POST':
        Student_ID = request.data.get('Student_ID')
        if Student_ID:
            try:
                student=Student.objects.get(Student_ID=Student_ID)
                student.delete()
                return Response({'status':'data deleted successfully!!!'},status=200)
            except Student.DoesNotExist:
                return Response({'status':'student does not exist'},status=404)
        else:
            return Response({'status':'Student_ID needed to delete'},status=500)