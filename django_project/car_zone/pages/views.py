from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse
from pages.models import Team
import json
from pages.models import *
def homepage(request):
        teams = Team.objects.all()
        data={
                'teams' : teams
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