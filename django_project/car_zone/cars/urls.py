from django.urls import path
from cars.views import *
urlpatterns = [
    path('',carspage,name='carspage')
]
