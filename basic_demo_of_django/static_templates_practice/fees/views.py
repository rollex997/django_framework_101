from django.shortcuts import render

# Create your views here.
def fees(request):
    fees = 'fees'
    dictionary = {'name':fees}
    return render(request,"fees/fees.html",context = dictionary)