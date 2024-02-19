from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from auth_api.models import *
# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        user = request.user
        user_id=user.id
        try:
            User_profile_DB = EmployeeProfile.objects.get(user=user_id)
            #Student
            #Teacher
            title_ = 'Home'
            data = {
                'title' : title_,
                'user_profile':User_profile_DB
            }
            return render(request,'home/homepage.html',data)
        except:
            return render(request,'home/homepage.html')
    else:
        return redirect(reverse('login'))
    