from functools import partial
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from viewSet.models import *
from viewSet.serializer import *
# Create your views here.
class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response({'data':serializer.data})
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
          try:
              student=Student.objects.get(ID=pk)
              serializer = StudentSerializer(student)
              return Response({'data':serializer.data})
          except Student.DoesNotExist:
              return Response({'status':'Data Does not exist'},status=404)
    def update(self,request,pk=None):
        id = pk
        if id is not None:
            try:
                student = Student.objects.get(ID=pk)
                serializer = StudentSerializer(student,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status':'data updated'},status=200)
                else:
                    return Response({'status':serializer.errors},status=400)
            except Student.DoesNotExist:
                return Response({'status':'Data does not exist'},status=404)
    def partial_update(self,request,pk=None):
        id = pk
        if id is not None:
            try:
                student = Student.objects.get(ID=pk)
                serializer = StudentSerializer(student,data=request.data,partial = True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status':'Data updated'},status=200)
                else:
                    return Response({'status':serializer.errors},status=400)
            except Student.DoesNotExist:
                return Response({'status':'Data does not exist'},status=404)
    def create(self,request):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':'Data created'},status=201)
            else:
                return Response({'status':serializer.errors},status=400)
        except:
            return Response({'status':'Internal server error'},status=500)
    def destroy(self,request,pk=None):
        id=pk
        if id is not None:
            try:
                student = Student.objects.get(ID=pk)
                student.delete()
                return Response({'status':'data deleted'},status=204)
            except Student.DoesNotExist:
                return Response({'status':'data not found'},status=404)