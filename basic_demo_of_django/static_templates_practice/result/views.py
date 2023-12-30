from django.shortcuts import render
from datetime import datetime
# Create your views here.
def result(request):
    dt = datetime.now()
    dictonary = {'dt' : dt}
    return render(request,"result/result.html",dictonary)