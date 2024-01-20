from django.shortcuts import render

# Create your views here.
def home(request):
    title_="Home"
    data = {'title' : title_}
    return render(request,'home/home.html',data);