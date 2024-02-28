from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse
from pages.models import Team
from cars.models import Car
import json
from pages.models import *
def homepage(request):
        teams = Team.objects.all()
        featured_cars = Car.objects.order_by('created_date').filter(is_featured=True)
        latest_cars = Car.objects.order_by('created_date')[:6]
        data={
                'teams' : teams,
                'featured_cars':featured_cars,
                'latest_cars':latest_cars
        }
        return render(request,'home/home.html',data)
def about_page(request):
        teams = Team.objects.all()
        data={
                'teams' : teams
        }
        return render(request,'about/about.html',data)
def services_page(request):
        return render(request,'services/services.html')
def contact_page(request):
        return render(request,'contact/contact.html')