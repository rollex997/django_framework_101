from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from task1.models import *
from task1.serializers import *
# Create your views here.

class StudentAPI(APIView):
    def post(self,request):
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201,'msg':'Data Created Successfully!!!'},status=201)
        else:
            return Response({'status':500,'error':serializer.errors},status=500)
    def put(self,request):
        id = request.data.get('id')
        try:
            student = Student.objects.get(id=id)
            serializer = StudentSerializers(student,data = request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'msg':'Data Updated!!'},status=200)
        except Student.DoesNotExist as e:
            return Response({'status':404,'error':e},status=404)
    def get(self,request):
        id = request.data.get('id')
        if id:
            #Get one data
            try:
                student = Student.objects.get(id=id)
                serializer = StudentSerializers(student)
                return Response({'status':200,'data':serializer.data},status=200)
            except Student.DoesNotExist as e:
                return Response({'status':500,'error':e},status=500)
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

from task1.tasks import *
class SendEmail(APIView):
    def post(self,request):
        name = request.data.get('name')
        email = request.data.get('email')
        review = request.data.get('review')
        print(f"name : {name}")
        print(f"email : {email}")
        print(f"review : {review}")
        if name and email and review:
            send_email_task.delay(name,email,review)
            return Response({'status':200},status=200)
        else:
            return Response({'status':500,'error':"Input fields can't be empty"},status=500)

