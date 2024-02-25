from rest_framework import serializers
from .models import Singer, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'duration']

class SingerSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True,read_only=True)
    class Meta:
        model = Singer
        fields = ['name', 'gender', 'songs']