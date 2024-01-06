from django.shortcuts import render

# Create your views here.
def results(request):
    marks = {'Rollex' : 99.99,
             'Leo' : 97,
             'Ballistic' : 94,
             'Barbatos' : 92,
             'Bullet' : 90,
             'Kraken' : 87
             }
    data = {'title' : 'result','messege' : 'This is a result page','data' : marks}
    return render(request,"result/result.html",data)