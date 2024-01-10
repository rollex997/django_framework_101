from django.shortcuts import render

# Create your views here.
def home(request):
    name = "Aditya Kumar"
    intro = "I am "
    intro2 = ", an ambitious and talented recent graduate, who is eager to embark on a career as a Python and Django Developer. Armed with a B.Tech in Computer Science and a solid foundation in programming concepts, I have a strong passion for web development and a determination to contribute innovative solutions in a professional setting."

    introduction ={'intro' : intro, 'name' : name , 'intro2': intro2}
    data = {'data' : introduction}
    return render(request,'core/home.html',data)