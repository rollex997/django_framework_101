from rest_framework import viewsets
from token_app.models import Student
from token_app.serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]