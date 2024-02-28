from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser

from pages.models import Team
from pages.serializer import TeamSerializers
from pages.pagination_api import MyPageNoPagination

from rest_framework_simplejwt.tokens import RefreshToken
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }

class TeamAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = MyPageNoPagination
    def get(self,request):
        paginator = self.pagination_class()
        Team_data = Team.objects.all()
        page = paginator.paginate_queryset(Team_data, request)

        serializer = TeamSerializers(page,many=True)
        return paginator.get_paginated_response({'data':serializer.data})

#admin operations api section
class TeamAdmin(APIView):
    # permission_classes = [IsAuthenticated,IsAdminUser]
    def post(self,request):
        serializer = TeamSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201},status=201)
        else:
            return Response({'status':200},status=200)
    def put(self,request):
        ID = request.data.get('id')
        try:
            team = Team.objects.get(id=ID)
            serializer = TeamSerializers(team,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200},status=200)
            else:
                return Response({'status':400},status=400)
        except Team.DoesNotExist:
            return Response({'errors':'Team does not exist'},status=404)
class TeamAdminDelete(APIView):
    # permission_classes = [IsAuthenticated,IsAdminUser]
    def delete(self,request):
        ID = request.data.get('id')
        try:
            team = Team.objects.get(id=ID)
            team.delete()
            return Response({'status':'team deleted'},status=200)
        except Team.DoesNotExist:
            return Response({'status':'team does not exist'},status=404)