from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.

def main(request):
    if request.user.is_authenticated:
            current_user = request.user
            user = User.objects.get(pk=current_user.id)
            title_ = "Main"
            data={
                'title':title_,
                'user':user
            }
            return render(request,'main/main.html',data)
    else:
       return redirect(reverse('login'))