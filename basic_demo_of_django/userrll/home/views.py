from django.shortcuts import render,redirect
from django.urls import reverse

# Create your views here.
def main(request):
    if request.user.is_authenticated:
        title_ = 'home'
        data={
            'title':title_
        }
        return render(request,'main/main.html',data)
    else:
        return redirect(reverse('register'))