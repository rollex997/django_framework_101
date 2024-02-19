from django.urls import path
from auth_api.views import *
urlpatterns = [
    path('',register,name="register"),
    path('registerUser',registerUser,name="registerUser"),
    path('verifyOTPpage',verifyOTPpage,name="verifyOTPpage"),
    path('verifyOTPProcess',verifyOTPProcess,name="verifyOTPProcess"),
    path('login',login,name="login"),
    path('loginUser',loginUser,name="loginUser"),
    path('logout',logout,name="logout"),
    path('forgetPasswordPage/<username>',forgetPasswordPage,name="forgetPasswordPage"),
    path('verifyOTPForgotPassword',verifyOTPForgotPassword,name="verifyOTPForgotPassword"),
    path('verify_email',verify_email,name="verify_email"),
    path('verify_email_otp_verify',verify_email_otp_verify,name="verify_email_otp_verify"),
]