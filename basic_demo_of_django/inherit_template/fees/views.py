from django.shortcuts import render

# Create your views here.
def fees(request):
    fees_ = {'service_charge' : 12000 , 
             'GST' : 4000,
             'Electronic_library' : 1200,
             'books' : 1500,
             'Lab' : 2000
             }
    data = {'title': "fees",'message':'This is a fees page','data' : fees_}
    return render(request,'fees/fees.html',data)