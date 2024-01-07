from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def fees(request):
    fees_ = {
        'Library' : 1200,
        'Canteen' : 2000,
        'Tuition_fees': 24000,
        'hostel_fees' : 50000
    }
    data = {'title' : 'fees', 'data' : fees_}
    return render(request, 'fees/fees.html', data)
def fees_api(request):
    fees_ = {
        'Library' : 1200,
        'Canteen' : 2000,
        'Tuition_fees': 24000,
        'hostel_fees' : 50000
    }
    data = {'title' : 'fees', 'data' : fees_}
    return JsonResponse(data)