from django.shortcuts import render

# Create your views here.
def course(request):
    students = {
        'stu1' : {'name' : 'Rollex' , 'roll_no' : 997},
        'stu2' : {'name' : 'Leo' , 'roll_no' : 967},
        'stu2' : {'name' : 'Ballistic' , 'roll_no' : 747},
        'stu3' : {'name' : 'Bullet', 'roll_no' : 380},
        'stu4' : {'name' : 'Barbatos' , 'roll_no' : 1090}
    }
    data = {'data' : students}
    return render(request,"course/course.html",context=data)