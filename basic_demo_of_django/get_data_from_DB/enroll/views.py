from django.shortcuts import render

# Create your views here.
def enroll(request):
    data = {'title' : 'Enroll'}
    return render(request,"enroll/enroll.html",data)