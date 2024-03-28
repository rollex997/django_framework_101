from django.urls import path
from auth_user.views import *
urlpatterns=[
    path('',registerPage,name="registerPage"),
    path('registerUser/',registerUser,name='registerUser'),
    path('resend_otp/',resendOtp,name="resendOtp"),
    path('registerVerifyOtpPage/',registerVerifyOtpPage,name='registerVerifyOtpPage'),
    path('verifyotpregister/',verifyOtpRegisterUser,name='verifyOtpRegisterUser'),
    path('loginUserPage/',loginUserPage,name="loginUserPage"),
    path('loginuser/',loginUser,name="loginUser"),
    path('GenerateResetPasswordPage/',GenerateResetPasswordPage,name="GenerateResetPasswordPage"),
    path('GenerateResetPasswordLink/',GenerateResetPasswordLink,name="GenerateResetPasswordLink"),
]