from django.shortcuts import render
from api.serializer import SongSerializer, SingerSerializer
from rest_framework import viewsets
from api.models import Singer, Song
# Create your views here.
class singerViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer
class songViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer
