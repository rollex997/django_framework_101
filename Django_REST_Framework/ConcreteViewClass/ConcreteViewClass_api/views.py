from django.shortcuts import render
from ConcreteViewClass_api.models import *
from ConcreteViewClass_api.serializer import *
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializers
class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
class StudentDelete(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

#combine class ConcereteView api
#class that do not require pk in dynamic link
class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
#classes that require pk in dynamic links
class StudentRetireveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers