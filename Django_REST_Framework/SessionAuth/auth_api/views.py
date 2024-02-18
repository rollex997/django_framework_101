from rest_framework import viewsets
from auth_api.models import Student
from auth_api.serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,DjangoModelPermissions
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]