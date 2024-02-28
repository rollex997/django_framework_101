from django.shortcuts import render
from django.http import JsonResponse
from cars.models import *
# Create your views here.

def carspage(request):
    return render(request,'cars/cars.html')

def CarDetailsPage(request,id):
    print(f"car id = {id}")
    car = Car.objects.get(id=id)
    data = {
        'car':car
    }
    return render(request,'car_detail/car_detail.html',data)