from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from task1.models import *
from task1.serializers import *
from django.views.generic import TemplateView
from django.db import IntegrityError
# Create your views here.
class StudentDashboardView(TemplateView):
    template_name = 'task1/student_dashboard.html' 


# STUDENT DETAILS RELATED API/FUNCTIONS STARTS
class StudentDetailsView(TemplateView):
    template_name = 'task1/Student_details.html' 
class StudentAPI(APIView):
    def post(self,request):
        serializer = StudentSerializers(data = request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201,'msg':'Data Created Successfully!!!'},status=201)
            else:
                return Response({'status':500,'error':serializer.errors},status=500)
        except IntegrityError:
            return Response({'status':500,'error':'Roll number must be unique'},status=500)
    def put(self,request):
        id = request.data.get('id')
        try:
            student = Student.objects.get(id=id)
            serializer = StudentSerializers(student,data = request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'msg':'Data Updated!!'},status=200)
            else:
                return Response({'status':500,'error':str(serializer.errors['roll'][0])},status=500)
        except Student.DoesNotExist as e:
            return Response({'status':404,'error':f"{e}"},status=404)
    def get(self,request,student_id=None):
        id = student_id
        if id:
            try:
                student = Student.objects.get(id=id)
                serializer = StudentSerializers(student)
                return Response({'status':200,'data':serializer.data},status=200)
            except Student.DoesNotExist as e:
                return Response({'status':400,'error':str(e)},status=400)
        else:
            #get all data
            student = Student.objects.all()
            serializer = StudentSerializers(student,many=True)
            return Response({'status':200,'data':serializer.data},status=200)
    def delete(self,request):
        id = request.data.get('id')
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return Response({'status':200,'msg':'Data Deleted'},status=200)
        except Student.DoesNotExist as e:
            return Response({'status':500,'error':e},status=500)
  # STUDENT DETAILS RELATED API/FUNCTIONS ENDS         