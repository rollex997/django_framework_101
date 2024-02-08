from django.urls import path
from auth_user.views import *
# path('verifyotp/<username>/<email>/<password>/<OTP>',verifyOTP,name="verifyotp"),
urlpatterns = [
    path('email_otp',email_otp,name="email_otp"),
    
    path('verifyotp',verifyOTP,name="verifyotp"),
    path('verifyOTPProcess',verifyOTPProcess,name="verifyOTPProcess"),
    path('register',register,name="register"),
    path('registerUser',registerUser,name="registerUser"),
    path('login',login,name="login"),
    path('loginUser',loginUser,name="loginUser"),
    path('logout',logout,name="logout"),
    path('changePassPage/<username>',changePassPage,name="changePassPage"),
    path('changepass',changepass,name="changepass"),
]
