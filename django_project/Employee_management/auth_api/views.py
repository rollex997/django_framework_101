from django.shortcuts import render,redirect
from django.urls import reverse
import json
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
import random
from auth_api.models import *
otp = []
user_data = {}
def verifyOTPpage(request):
   if not request.user.is_authenticated:
       return render(request,'auth_api/verifyOTPpage.html')
   else:
       return redirect(reverse('main'))
def verifyOTPProcess(request):
       is_ajax = request.headers.get('X-Requested-With')=='XMLHttpRequest'
       if is_ajax:
           if request.method=='POST':
               print(f"otp : {otp}")
               if len(otp)!=0:
                   data = json.load(request)
                   otp_entered = data.get('payload')
                   otp_E = otp_entered['otp']
                   print(f'stored otp : {otp[0]}')
                   print(f'stored user_data : {user_data}')
                   if int(otp_E)==otp[0]:
                       user = User.objects.get(username=user_data['username'])
                       user.is_active = True
                       user.save()
                       return JsonResponse({'status':200},status=200)
                   else:
                       return JsonResponse({'status':404},status=404)
               else:
                   return JsonResponse({'status':400},status=400)
def register(request):
   if not request.user.is_authenticated:
     return render(request,'auth_api/register.html')
def registerUser(request):
   global user_data
   global otp
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
               # Set the is_active attribute to False
               user.is_active = False
               user.save()
               EmployeeProfile.objects.create(
                   user = user,
                   phone=user_data['phone']
                   )
               
               email_addr = user_data['email']
               username = user_data['username']
               password = user_data['password1']
                # Prepare email
               otp.clear()
               otp.append(random.randint(1000, 9999999))
               print(f"otp saved : {otp}")
               subject = f"{username} please verify OTP"
               message = "verify your OTP " + str(otp[0])
               recipient_list = [email_addr]
    
    
               # Create EmailMessage object and attach the Excel file
               email = EmailMessage(subject, message, 'rollex68125@gmail.com', recipient_list)
    
    
               # Send the email
               email.send()
               email_addr=""
               user_data.clear()
               user_data.update(
                   {'username':username,
                   'email':email_addr,
                   'password':password,}
               )
               print(f"saved user_data: {user_data}")
               return JsonResponse({'status':200},status=200)
   else:
       return redirect(reverse('main'))
def login(request):
   if not request.user.is_authenticated:
       return render(request,'auth_api/login.html')
   else:
       return redirect(reverse('homepage'))
def loginUser(request):
   is_ajax = request.headers.get('X-Requested-With')=='XMLHttpRequest'
   if is_ajax:
       if request.method=='POST':
           data = json.load(request)
           user_data = data.get('payload')
           username = user_data['username']
           password = user_data['password']
           user = authenticate(username=username,password=password)
           if user:
               print(user)
               auth_login(request,user)
               return JsonResponse({'status':200},status=200)
           else:
               return JsonResponse({'status':400},status=400)
def logout(request):
    if request.user.is_authenticated:
       is_ajax=request.headers.get('X-Requested-With')=='XMLHttpRequest'
       if is_ajax:
           if request.method=='POST':
               auth_logout(request)
               return JsonResponse({'status':200},status=200)
           else:
               return JsonResponse({'status':400},status=400)
# def changePassPage(request,username):
#    if request.user.is_authenticated:
#         data={
#              'username':username
#         }
#         return render(request,'auth_user/ChangePassword.html',data)
#    else:
#        return redirect(reverse('register'))
# def changepass(request):
#    is_ajax = request.headers.get("X-Requested-With")=="XMLHttpRequest"
#    if is_ajax:
#        if request.method=='POST':
#            data = json.load(request)
#            user_data = data.get('payload')
#            username=user_data['username']
#            passOLD=user_data['passOLD']
#            newpass = user_data['pass1']
#            user = authenticate(username=username,password=passOLD)
#            user.set_password(newpass)
#            user.save()
#            user = authenticate(username=username,password = newpass)
#            auth_login(request,user)
#            return JsonResponse({'status':200},status=200)
def forgetPasswordPage(request,username):
   if not request.user.is_authenticated:
       user_data.clear()
       user_data.update({
           'username':username
       })
       print(f"user_data forgot password: {user_data}")
       return render(request,'auth_api/forgotpasswordPage.html')
   else:
       return redirect(reverse('homepage'))
def verifyOTPForgotPassword(request):
   is_ajax=request.headers.get("X-Requested-With")=="XMLHttpRequest"
   if is_ajax:
       if request.method=='POST':
           data = json.load(request)
           user_password = data.get('payload')
           username = user_data['username']

           try:
              user = User.objects.get(username=username)
              otp.clear()
              otp.append(random.randint(100,999999999))
              subject = f"{user_data['username']} please verify OTP"
              message = "verify your OTP " + str(otp[0])
              email_addr = user.email
              recipient_list = [email_addr]
 
              # Create EmailMessage object and attach the Excel file
              email = EmailMessage(subject, message, 'rollex68125@gmail.com', recipient_list)
 
              # Send the email
              email.send()
              email_addr=""
              user_data.clear()
              user_data.update(
                   {'username':user.username,
                   'email':user.email,
                   'password':user_password['password'],}
              )
              return JsonResponse({'status':200},status=200)
           except User.DoesNotExist:
                  return JsonResponse({'status':404},status=404)
def verify_email(request):
   if not request.user.is_authenticated:
       return render(request,'auth_api/verify_email_page.html')
   else:
       return render(reverse('main'))
def verify_email_otp_verify(request):
   is_ajax = request.headers.get('X-Requested-With')=='XMLHttpRequest'
   if is_ajax:
       if request.method=='POST':
           data=json.load(request)
           otp_frontend = data.get('payload')
           saved_user = user_data
           otp_f = otp_frontend['otp']
           print(f"saved otp : {otp[0]}")
           print(f"otp coming from front : {otp_f}")
           print(saved_user)


           if len(otp)!=0:
               if int(otp_f) == otp[0]:
                   try:
                       user = User.objects.get(username=saved_user['username'])
                       print(f"db user : {user.username}")
                       print(f"db user : {user.password}")
                       user.set_password(saved_user['password'])
                       user.save()
                       return JsonResponse({'status':200},status=200)
                   except User.DoesNotExist:
                       return JsonResponse({'status':402},status=402)
               else:
                   return JsonResponse({'status':404},status=404) #otp did not matched
           else:
               return JsonResponse({'status':400},status=400) #error try again