from django.shortcuts import render

# Create your views here.
def course(request):
    items = {'course' : 'course', 'messege' : 'this is a course page'}
    data = {'data' : items}
    return render(request,'course/course.html', data)