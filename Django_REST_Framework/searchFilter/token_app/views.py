from rest_framework import viewsets
from token_app.models import *
from token_app.serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
class StudentModelViewSet(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[SearchFilter]
    # search_fields=['city','name']
    search_fields=['^city','^name']