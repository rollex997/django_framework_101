from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from pages.models import Team
from pages.serializer import TeamSerializers

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }

class TeamAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        Team_data = Team.objects.all()
        serializer = TeamSerializers(Team_data,many=True)
        return Response({'data':serializer.data},status=200)