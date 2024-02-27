from pages.models import Team
from rest_framework import serializers
class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id','firstname','lastname','designation','photo','facebook_link','twitter_link']
        read_only_fields = ['id',]