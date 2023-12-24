from django.shortcuts import render

# Create your views here.
#this function will return home html
def home(request):
    return render(request,"home.html")

# this function will return course html
def course(request):
    return render(request,"course.html")

#this function will return fees html
def fees(request):
    return render(request, "fees.html")

#this function will return result html
def result(request):
    return render(request, "result.html")