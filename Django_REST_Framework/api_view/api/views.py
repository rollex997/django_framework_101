from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models import *
from api.serializers import *
# Create your views here. 
@api_view(['POST'])
def create_student(request):
    if request.method=='POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'data inserted'},status=200)
        else:
            return Response({'status':serializer.errors},status=400)
@api_view(['PUT'])
def update_student(request, pk):
    if request.method == 'PUT':
        try:
            student = Student.objects.get(Student_ID=pk)
            serializer = StudentSerializers(student, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'Student updated successfully'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({'status': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def get_all_student(request):
    if request.method=='GET':
        student = Student.objects.all()
        serializer = StudentSerializers(student,many=True)
        return Response({'data':serializer.data})
@api_view(['GET'])
def get_one_student(request,pk):
    if request.method=='GET':
        try:
            student = Student.objects.get(Student_ID=pk)
            serializer = StudentSerializers(student)
            return Response({'data':serializer.data})
        except Student.DoesNotExist:
            return Response({'status':'student does not exist'})
@api_view(['DELETE'])
def delete_student(request,pk):
    if request.method=='DELETE':
        try:
            student = Student.objects.get(Student_ID=pk)
            student.delete()
            return Response({'status':'data deleted successfully!!!'})
        except Student.DoesNotExist:
            return Response({'status':'student does not exist'})
