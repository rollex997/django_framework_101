from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from auth_api.models import *
from django.http import JsonResponse
import json
from home.models import EmployeeExperience
# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        user = request.user
        user_id=user.id
        try:
            User_profile_DB = EmployeeProfile.objects.get(user=user_id)
            #Student
            #Teacher
            title_home = 'Home'
            title_employee = 'Employee'
            data = {
                'title_home' : title_home,
                'title_employee' : title_employee,
                'user_profile':User_profile_DB
            }
            return render(request,'home/homepage.html',data)
        except:
            return render(request,'home/homepage.html')
    else:
        return redirect(reverse('login'))
    
def empWorkCreate(request):
    if request.user.is_authenticated:
        is_ajax = request.headers.get("X-Requested-With")=="XMLHttpRequest"
        if is_ajax:
            if request.method=='POST':
                json_data = json.load(request)
                data = json_data.get('payload')
                try:
                    EmployeeExperience.objects.create(
                       company_name = data['company_name'],
                       role = data['role'],
                       date_of_joining = data['date_of_joining'],
                       last_date = data['last_date'],
                   )
                    return JsonResponse({'status':201},status=201)
                except:
                    return JsonResponse({'status':500},status=500)

def empWorkRead(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                data = list(EmployeeExperience.objects.all().values())
                return JsonResponse({'context': data}, status=200)
            else:
                return JsonResponse({'status': 'Invalid request: not AJAX'}, status=402)
        else:
            return JsonResponse({'status': 'Invalid request method: not POST'}, status=400)
    else:
        return JsonResponse({'status': 'Unauthorized'}, status=401)
    
def empEdit(request):
    if request.user.is_authenticated:
        is_ajax = request.headers.get("X-Requested-With")=="XMLHttpRequest"
        if is_ajax:
            if request.method=='POST':
                json_data = json.load(request)
                data = json_data.get('payload')
                print(data)
                try:
                    employee_experience = EmployeeExperience.objects.get(ID = data['ID'])
                    employee_experience.company_name = data['company_name']
                    employee_experience.role = data['role']
                    employee_experience.date_of_joining = data['date_of_joining']
                    employee_experience.last_date = data['last_date']
                    employee_experience.save()
                    return JsonResponse({'status':200},status=200)
                except EmployeeExperience.DoesNotExist:
                    return JsonResponse({'status':400},status=400)

def empdelete(request):
    if request.user.is_authenticated:
        is_ajax = request.headers.get("X-Requested-With")=="XMLHttpRequest"
        if is_ajax:
            if request.method=='POST':
                json_data = json.load(request)
                data=json_data.get('payload')
                try:
                    emp = EmployeeExperience.objects.get(ID=data['ID'])
                    emp.delete()
                    return JsonResponse({'status':200},status=200)
                except EmployeeExperience.DoesNotExist:
                    return JsonResponse({'status':400},status=400)
