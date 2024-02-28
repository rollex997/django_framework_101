from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def carspage(request):
    return render(request,'cars/cars.html')
def cars(request):
    is_ajax = request.headers.get("X-Requested-With")=='XMLHttpRequest'
    if is_ajax:
        if request.method=='POST':
            pass