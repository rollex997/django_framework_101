from django.urls import path
from auth_api.views_api import *
urlpatterns = [
 path('registerUser_api',registerUser,name='registerUser_api'),
 path('email_verification_api',email_verification,name='email_verification_api'),
 path('loginUser_api',loginUser,name='loginUser_api'),
 path('logoutUser_api',logoutUser,name='logoutUser_api'),
 path('forgotPassword',forgotPassword,name='forgotPassword'),
 path('verify_otp_forgotpassword',verify_otp_forgotpassword,name='verify_otp_forgotpassword'),
]
