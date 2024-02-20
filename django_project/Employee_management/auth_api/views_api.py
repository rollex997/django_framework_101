from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from auth_api.models import *
from django.contrib.auth.models import User
from auth_api.serializer import *
import random
from django.core.mail import EmailMessage
from Employee_management.settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
#otp dictionary
'''
{
    "user": {
        "username": "aastha",
        "email": "aryan268859@gmail.com",
        "password": "iloveironman"
    },
    "phone": "1234567890"
}
'''
otp = {}
data_global = {}
@api_view(['POST'])
def registerUser(request):
   if not request.user.is_authenticated:
     if request.method == 'POST':
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                OTP = random.randint(1000, 9999)
                otp.clear()
                otp.update({"otp":OTP})
                print(f"saved otp : {otp}")
                user = request.data.get('user')
                username = user['username']
                email_ = user['email']
                data_global.clear()
                data_global.update({"username":f"{username}" , "email" : f"{email_}"})
                print(f"saved username : {data_global}")

                #send OTP via email
                try:
                    email_addr = data_global['email']
                    subject = f"{data_global['username']} please verify OTP"
                    message = "verify your OTP " + str(otp['otp'])
                    recipient_list = [email_addr]     
                    # Create EmailMessage object and attach the Excel file
                    email = EmailMessage(subject, message, EMAIL_HOST_USER, recipient_list)
                    # Send the email
                    email.send()
                    email_addr=""

                    return Response({'status':200},status=200)# email sent
                except:
                     return Response({'status':400},status=400) #something went wrong email
            else:
                return Response({'status': serializer.errors}, status=400)
'''
{
"otp":1234
}
'''
@api_view(['POST'])
def email_verification(request):
   if not request.user.is_authenticated:
     if request.method=='POST':
          OTP = request.data.get('otp')
          try:
              if OTP == otp['otp']:
                  print(f"OTP == otp : {OTP} True")
                  try:
                    username = data_global['username']
                    print(f"saved username : {username}")
                    user=User.objects.get(username=username)
                    print(user)
                    user.is_active=True
                    user.save()
                    return Response({'status':200},status=200)
                  except User.DoesNotExist:
                       return Response({'status':404},status=404)#User does not exist
              else:
                   return Response({'status':402},status=402)#otp dint match
          except:
               return Response({'status':500},status=500)#Something went wrong
'''
{
"username":"aditya",
"password":"aditya"
}
'''
@api_view(['POST'])
def loginUser(request):
   if not request.user.is_authenticated:
     if request.method=='POST':
          username = request.data.get('username')
          password = request.data.get('password')
          print(f"username : {username}, password : {password}")
          user = authenticate(username = username,password = password)
          if user:
               auth_login(request,user)
               return Response({'status':200},status=200)
          else:
               return Response({'status':400},status=400)
@api_view(['POST'])
def logoutUser(request):
   if request.user.is_authenticated:
     if request.method=='POST':
          try:
              auth_logout(request)
              return Response({'status':200},status=200)
          except:
              return Response({'status':400},status=400)
'''
{
"username":"aastha",
"password":"12345",
"password2":"12345"
}
'''
@api_view(['POST'])
def forgotPassword(request):
   if not request.user.is_authenticated:
     if request.method=='POST':
          username = request.data.get('username')
          password = str(request.data.get('password'))
          password2 = str(request.data.get('password2'))
          print(f"username : {username}, password : {password}, password2 : {password2}")
          if password == password2:
              try:
                   user = User.objects.get(username=username)
                   #generate otp
                   OTP = random.randint(1000, 9999)
                   otp.clear()
                   otp.update({"otp":OTP})
                   print(f"forgot password saved otp : {otp}")
    
                   #save the user 
                   data_global.clear()
                   data_global.update({
                        'username':username,
                        'password':password,
                   })
                   print(f"forgot password saved data_global : {data_global}")
                   email = user.email
                   print(email)
                   #send OTP via email
                   try:
                        email_addr = email
                        subject = f"{username} please verify OTP"
                        message = "verify your OTP " + str(otp['otp'])
                        recipient_list = [email_addr]     
                        # Create EmailMessage object and attach the Excel file
                        email = EmailMessage(subject, message, EMAIL_HOST_USER, recipient_list)
                        # Send the email
                        email.send()
                        email_addr=""
                        return Response({'status':200},status=200)# email sent
                   except:
                         return Response({'status':400},status=400) #something went wrong email
              except User.DoesNotExist:
                   return Response({'status':404},status=404) # user not found
          else:
               return Response({'status':406},status=406) # password din't match
'''
{
"otp":9634
}
'''
@api_view(['POST'])
def verify_otp_forgotpassword(request):
   if not request.user.is_authenticated:
     if request.method=='POST':
          otp_f = request.data.get('otp')
          otp_s = otp['otp']
          username = data_global['username']
          password = data_global['password']
          if otp_s:
              if otp_f==otp_s:
                   user = User.objects.get(username=username)
                   user.set_password(password)
                   user.save()
                   return Response({'status':200},status=200) # send the user to the login page
              else:
                   return Response({'status':401},status=401) # otp din't match
          else:
               return Response({'status':400},status=400)
