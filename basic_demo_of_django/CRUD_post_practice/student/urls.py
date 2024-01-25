from django.urls import path
from student.views import *
urlpatterns = [
    path('',student,name="student"),
    path('insert_student_info',insert_student_info,name='insert_student_info'),
    path('Read_student_info',Read_student_info,name='Read_student_info'),
    path('Update_student_info',Update_student_info,name='Update_student_info'),
    path('delete_student_info',delete_student_info,name='delete_student_info'),
]
