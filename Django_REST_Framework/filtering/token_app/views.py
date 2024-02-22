from rest_framework import viewsets
from token_app.models import Student
from token_app.serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
class StudentModelViewSet(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get_queryset(self):
        user =self.request.user
        return Student.objects.filter(passby=user)