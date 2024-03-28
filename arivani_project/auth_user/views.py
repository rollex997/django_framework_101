from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from auth_user.models import UserProfile
from django.contrib.auth import login as login_user
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_user
from django.db import IntegrityError
import json
import random

from django.utils.encoding import smart_str, force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# Create your views here.
def registerPage(request):
    title = "register"
    data = {
        'title':title,
    }
    return render (request,'auth_user/register_page.html',data)
role_list = ['Teacher','Student']
otp_save = {}
user_save = {}
def registerUser(request):
    is_ajax = request.headers.get("X-Requested-With")=='XMLHttpRequest'
    if is_ajax:
        if request.method=='POST':
            try:
                data = json.load(request)
                user_data = data.get('payload')
                username = user_data['username']
                email = user_data['email']
                password1 = user_data['password1']
                password2 = user_data['password2']
                role = user_data['role']
                if password1 == password2:
                    if role_list[0] == role or role_list[1] == role:
                        user = User.objects.create(
                            username = username,
                            email = email,
                        )
                        user.set_password('password1')
                        user.is_active=False
                        user.save()
                        UserProfile.objects.create(
                            user = user,
                            role = role
                        )

                        # generate a random otp
                        user_save.clear()
                        user_save['email'] = email
                        user_save['username'] = username
                        otp_save.clear()
                        otp_save['otp'] = random.randint(1000,9999)
                        print(otp_save)
                        #send otp via email
                        return JsonResponse({'status':200},status=200)
                    else:
                        return JsonResponse({'status':500,'error':'Role error'},status=500)
                else:
                    return JsonResponse({'status':500,'error':"Password don't match"})
            except IntegrityError as e:
                return JsonResponse({'status':500,'error':'username taken'},status=500)
        else:
            return JsonResponse({'status':400,'error':'bad request'},status=400)

def registerVerifyOtpPage(request):
    title='Verify Otp'
    data={
        'title':title
    }
    return render(request,'auth_user/register_verify_otp.html',data)
def resendOtp(request):
    is_ajax = request.headers.get("X-Requested-With")=="XMLHttpRequest"
    if is_ajax:
        if request.method=='POST':
            otp_save.clear()
            otp_save['otp'] = random.randint(1000,9999)
            print(otp_save)
            #send otp via email
            return JsonResponse({'status':200},status=200)
        else:
            return JsonResponse({'status':400,'error':'Bad Request'},status=400)
def verifyOtpRegisterUser(request):
    is_ajax = request.headers.get("X-Requested-With")=='XMLHttpRequest'
    if is_ajax:
        if request.method=='POST':
            data = json.load(request)
            otp_data = data.get('payload')
            if int(otp_data['otp']) == int(otp_save['otp']):
                try:
                    user = User.objects.get(username = user_save['username'])
                    user.is_active = True
                    user.save()
                    return JsonResponse({'status':200},status=200)
                except User.DoesNotExist:
                    return JsonResponse({'status':404,'error':'User does not exist'},status=404)
            else:
                return JsonResponse({'status':500,'error':"otp din't match"},status=500)
        else:
            return JsonResponse({'status':400,'error':'bad request'},status=400)

def loginUserPage(request):
    title='Login user'
    data={
        'title':title
    }
    return render(request,'auth_user/loginUser.html',data)
def loginUser(request):
    is_ajax = request.headers.get("X-Requested-With")=="XMLHttpRequest"
    if is_ajax:
        if request.method=='POST':
            data = json.load(request)
            login_data = data.get('payload')
            username = login_data['username']
            password = login_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login_user(request,user)
                return JsonResponse({'status':200},status=200)
            else:
                return JsonResponse({'status':404,'error':'Bad User credentials'},status=404)
        else:
            return JsonResponse({'status':400,'error':'Bad request'},status=400)
def GenerateResetPasswordPage(request):
    title="Reset Password Link"
    data={
        'title':title
    }
    return render(request,'auth_user/generateResetPasswordLink.html',data)
def GenerateResetPasswordLink(request):
    try:
        username = login_data['username']
        user = Customer.objects.get(username=username)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = PasswordResetTokenGenerator().make_token(user)
        link = f'http://http://127.0.0.1:8000/resetPassword/{uid}/{token}'
        print(f"reset password link : {link}")
        return JsonResponse({'status':200},status=200)
    except:
        return JsonResponse({'status':500,'error':'Bad request'},status=500)