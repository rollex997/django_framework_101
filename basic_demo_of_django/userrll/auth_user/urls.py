from django.urls import path
from auth_user.views import *
urlpatterns = [
    path('register',register,name="register"),
    path('registerUser',registerUser,name="registerUser"),
    path('login',login,name="login"),
    path('loginUser',loginUser,name="loginUser"),
    path('logout',logout,name="logout"),
    path('changePassPage/<username>',changePassPage,name="changePassPage"),
    path('changepass',changepass,name="changepass"),
]
