from django.shortcuts import render
from mixin_api.models import *
from mixin_api.serializer import *
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
# Create your views here.

#list and create --> pk not required
class StudentListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    #to retireve all records
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    # to create a record
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

#retrieve , update, delete --> reqires pk
class StudentUpdateRetireveDelete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    #to retireve a single record
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    #to update a record
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    # to delete a record
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)