from django.shortcuts import render

# Create your views here.
def course(request):
    course_ = {

        'IT' : 'Information Technology',
        'CS' : 'Computer Science',
        'ENTC' : "Electronics and Telecommunications",
        "MECH" : "Mechanical Engineering"
    }
    data = {'data' : course_, 'title' : 'course'}
    return render(request, "course/course.html", data)