from django.urls import path
from student.views import *
urlpatterns = [
    path('', student,name="student"),
    path('insert_student_info',insert_student_info,name="insert_student_info"),
    path('get_student_info',get_student_info,name="get_student_info"),
    path('update_student_info',update_student_info,name="update_student_info"),
    path('delete_student_info',delete_student_info,name="delete_student_info"),
]
