from rest_framework import viewsets
from jwt_app.models import Student
from jwt_app.serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]