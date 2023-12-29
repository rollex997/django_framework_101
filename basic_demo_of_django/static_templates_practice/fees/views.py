from django.shortcuts import render

# Create your views here.
def fees(request):
    fees = 504658
    name = 'aditya Kumar'
    city = 'Lucknow'
    addr = 'asdfgh qwert'
    dictionary = {'name_' : name,'fees_':fees, 'city_' : city, 'addr' : addr}
    return render(request,"fees/fees.html",context = dictionary)