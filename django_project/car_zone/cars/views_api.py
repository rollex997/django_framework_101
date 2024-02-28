from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cars.models import Car
from cars.serializer import CarAdminSerializer, CarSerializer
from cars.pagination_api import *

from rest_framework_simplejwt.tokens import RefreshToken
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }
class Cars(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = MyPagination
    def get(self,request):
        paginator = self.pagination_class()
        car_data = Car.objects.all()
        page=paginator.paginate_queryset(car_data,request)
        serializer = CarSerializer(page,many=True)
        return paginator.get_paginated_response({'data':serializer.data, 
                                                 'state_choices':Car.state_choice, 
                                                 'year_choices':Car.year_choice,
                                                 'features_choices':Car.features_choices,
                                                 'door_choices':Car.door_choices
                                                 })

class FeaturedCars(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    pagination_class = FeaturedCarsPagination
    def get(self,request):
        paginator = self.pagination_class()
        car_data = Car.objects.order_by('created_date').filter(is_featured=True)
        page=paginator.paginate_queryset(car_data,request)
        serializer = CarSerializer(page,many=True)
        return paginator.get_paginated_response({
            'data':serializer.data
        })
    
class LatestCars(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    pagination_class = LatestCarPagination
    def get(self,request):
        paginator = self.pagination_class()
        car_data=Car.objects.order_by('created_date')[:6]
        page = paginator.paginate_queryset(car_data,request)
        serializer = CarSerializer(page,many=True)
        return paginator.get_paginated_response(
            {
                'data':serializer.data
            }
        )
    
#Admin Operations api section
class CarAdmin(APIView):
    # permission_classes = [IsAuthenticated,IsAdminUser]
    def post(self,request):
        serializer = CarAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201},status=201)
        else:
            return Response({'errors':serializer.errors},status=400)
    def put(self,request):
        ID = request.data.get('id')
        try:
             car = Car.objects.get(id=ID)
             serializer = CarAdminSerializer(car,data=request.data,partial=True)
             if serializer.is_valid():
                 serializer.save()
                 return Response({'status':200},status=200)
             else:
                 return Response({'errors':serializer.errors},status=400)        
        except Car.DoesNotExist:
            return Response({'errors':'Car does not exist'},status=404)

class CarAdminDelete(APIView):
    # permission_classes = [IsAuthenticated,IsAdminUser]
    def delete(self,request):
        ID = request.data.get('id')
        try:
            car = Car.objects.get(id=ID)
            car.delete()
            return Response({'status':'car deleted'},status=200)
        except Car.DoesNotExist:
            return Response({'errors':'Car does not exist'},status=404)