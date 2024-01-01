import datetime
from django.shortcuts import render

# Create your views here.
def result(request):
    dt = datetime.now()
    p1 = 56.24321
    p2 = 56.0000
    p3 = 56.37000
    p4 = 59.69999
    # if tag with 
    dictonary = {'dt' : dt, 'p1' : p1 , 'p2' : p2 , 'p3' : p3, 'p4' : p4}
    return render(request,"result/result.html",dictonary)
