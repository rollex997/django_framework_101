from django.http import JsonResponse
from django.shortcuts import render
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
# Create your views here.
def register(request):
    return render(request,'auth_user/register.html')
def registerUser(request):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            reg_user_data = data.get('payload')
            user = User.objects.filter(username = reg_user_data['username'])
            print(user)
            if user.exists():
                return JsonResponse({'status':599},status=599)
            user = User.objects.create(
                username = reg_user_data['username'],
                email = reg_user_data['email']
            )
            user.set_password(reg_user_data['password1'])
            user.save()
            return JsonResponse({'status':200},status=200)
        else:
            return JsonResponse({'status':400},status=400)

def login(request):
    return render(request,'auth_user/login.html')
def loginUser(request):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    if is_ajax:
        if request.method == 'POST':
            data = json.loads(request.body)
            login_user_data = data.get('payload')
            user = authenticate(username=login_user_data['username'], password=login_user_data['pass'])
            print(user)
            if user is not None:
                auth_login(request, user)
                return JsonResponse({'status': 200}, status=200)
            else:
                return JsonResponse({'status': 400}, status=400)
            
def logout(request):
    pass