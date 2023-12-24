from django.shortcuts import render,redirect

# Create your views here.
def fees(request):
    return render(request,'fees.html')