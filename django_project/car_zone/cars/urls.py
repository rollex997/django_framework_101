from django.urls import path
from cars.views import *
urlpatterns = [
    path('',carspage,name='carspage'),
    path('car_details/<int:id>',CarDetailsPage,name='car_details'),
]
