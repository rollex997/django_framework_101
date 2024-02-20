from functools import partial
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from home.models import EmployeeExperience
from auth_api.models import EmployeeProfile
from home.serializer import EmployeeExperienceSerializers
#authentication and permission
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def homepage_api(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            user = request.user
            employee_profile = EmployeeProfile.objects.get(user=user)
            data={
                'username':user.username,
                'email':user.email,
                'phone':employee_profile.phone
            }
            return Response({'user':data},status=200)

'''
['ID','company_name','role','date_of_joining','last_date']
create data
{
  "company_name": "Aditya Kuamr",
  "role": "Javascript Developer",
  "date_of_joining": "2022-1-1",
  "last_date": "2024-12-30"
}

update data (Complete)
{
  "ID":1,
  "company_name": "Aditya Kuamr",
  "role": "Javascript Developer",
  "date_of_joining": "2022-1-1",
  "last_date": "2024-12-30"
}
update data (partial update)
{
  "ID":1,
  "date_of_joining": "2022-1-1",
  "last_date": "2024-12-30"
}
'''
@api_view(['POST','PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def empWorkCreate_or_empWorkUpdate(request):
    if request.user.is_authenticated:
        print(request.data)
        if request.method=='POST':
            serializer = EmployeeExperienceSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200},status=200)
            else:
                return Response({'status':serializer.errors},status=400)
        if request.method=='PUT':
             ID = request.data.get('ID')
             emp = EmployeeExperience.objects.get(ID=ID)
             serializer = EmployeeExperienceSerializers(emp,data=request.data,partial=True)
             if serializer.is_valid():
                  serializer.save()
                  return Response({'status':201},status=201)
             else:
                  return Response({'status':400},status=400)

'''
to get one record
{
"ID":7
}
'''
@api_view(['GET','POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def empReadAll_OR_one(request):
    if request.user.is_authenticated:
        ID = request.data.get('ID')
        if ID:
              try:
                  emp = EmployeeExperience.objects.get(ID=ID)
                  serializer = EmployeeExperienceSerializers(emp)
                  return Response({'data':serializer.data},status=200)
              except EmployeeExperience.DoesNotExist:
                  return Response({'status':404},status=404)
        else:
            emp = EmployeeExperience.objects.all()
            serializer = EmployeeExperienceSerializers(emp,many=True)
            return Response({'data':serializer.data},status=200)
'''
Delete data
{
"ID":8
}
'''
@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def empDelete(request):
     if request.user.is_authenticated:
         if request.method=='POST':
              ID =  request.data.get('ID')
              if ID : 
                   try:
                        emp = EmployeeExperience.objects.get(ID=ID)
                        emp.delete()
                        return Response({'status':200},status=200)
                   except EmployeeExperience.DoesNotExist:
                        return Response({'status':404},status=404)
              else:
                   return Response({'status':400},status=400)