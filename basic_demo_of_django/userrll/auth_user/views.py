import re
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.middleware.csrf import CsrfViewMiddleware
# Create your views here.
def register(request):
    return render(request,'auth_user/register.html')
def registerUser(request):
    if not request.user.is_authenticated:
        is_ajax = request.headers.get("X-Requested-With")=="XMLHttpRequest"
        if is_ajax:
            if request.method=='POST':
                data = json.load(request)
                user_data = data.get('payload')
                print(user_data)
                user = User.objects.create(
                    username = user_data['username'],
                    email = user_data['email'],
                )
                user.set_password(user_data['password1'])
                user.save()
                return JsonResponse({'status':200},status=200)
    else:
        return redirect(reverse('main'))
        
def login(request):
    if not request.user.is_authenticated:
        return render(request,'auth_user/login.html')
    else:
        return redirect(reverse('main'))
def loginUser(request):
    is_ajax = request.headers.get('X-Requested-With')=='XMLHttpRequest'
    if is_ajax:
        if request.method=='POST':
            data = json.load(request)
            user_data = data.get('payload')
            username = user_data['username']
            password = user_data['pass']
            user = authenticate(username=username,password=password)
            if user:
                print(user)
                auth_login(request,user)
                return JsonResponse({'status':200},status=200)
            else:
                return JsonResponse({'status':400},status=400)
def logout(request):
    is_ajax=request.headers.get('X-Requested-With')=='XMLHttpRequest'
    if is_ajax:
        if request.method=='POST':
            auth_logout(request)
            return JsonResponse({'status':200},status=200)
def changePassPage(request,username):
    if request.user.is_authenticated:
         data={
              'username':username
         }
         return render(request,'auth_user/forgotPassword.html',data)
    else:
        return redirect(reverse('register'))
def changepass(request):
    is_ajax = request.headers.get("X-Requested-With")=="XMLHttpRequest"
    if is_ajax:
        if request.method=='POST':
            data = json.load(request)
            user_data = data.get('payload')
            username=user_data['username']
            passOLD=user_data['passOLD']
            newpass = user_data['pass1']
            user = authenticate(username=username,password=passOLD)
            user.set_password(newpass)
            user.save()
            user = authenticate(username=username,password = newpass)
            auth_login(request,user)
            return JsonResponse({'status':200},status=200)