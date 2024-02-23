from django.shortcuts import render
from api.serializer import songSerializers, singerSerializers
from rest_framework import viewsets
from api.models import Singer, Song
# Create your views here.
class singerViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=singerSerializers
class songViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=songSerializers
