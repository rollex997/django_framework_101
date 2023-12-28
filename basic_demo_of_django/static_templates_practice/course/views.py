from django.shortcuts import render

# Create your views here.
def course(request):
    h1_name = {'page_name' : 'course'}
    return render(request,"course/course.html",context=h1_name)