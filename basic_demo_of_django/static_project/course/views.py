from django.shortcuts import render

# Create your views here.
def course(request):
    Course = {'IT' : 'Information Technology',
              'CS' : 'Computer Science',
              'E' : 'electrical',
              'ELEC' : 'electronics'}
    context = {'Course' : Course}
    return render(request,'course.html',context)