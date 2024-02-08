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

    path('forgetPasswordPage/<username>',forgetPasswordPage,name="forgetPasswordPage"),
    path('verify_email',verify_email,name="verify_email"),
    path('verify_email_otp_verify',verify_email_otp_verify,name="verify_email_otp_verify"),
    path('verifyOTPForgotPassword',verifyOTPForgotPassword,name="verifyOTPForgotPassword"),
    
]