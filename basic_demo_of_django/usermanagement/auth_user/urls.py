from django.urls import path
from auth_user.views import *
urlpatterns = [
    path('login',login,name='login'),
    path('loginUser',loginUser,name='loginUser'),
    path('register',register,name='register'),
    path('registerUser',registerUser,name='registerUser'),
]
