from django.shortcuts import render

# Create your views here.
def home(request):
    dictionary = {'title' : 'Home' , 'heading' : 'This is a Home page'}
    return render(request,'home/home.html', dictionary)