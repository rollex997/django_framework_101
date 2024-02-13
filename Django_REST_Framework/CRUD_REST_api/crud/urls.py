from django.urls import path
from crud.views import *
urlpatterns = [
    path('',get_all_student,name='get_all_student'),
    path('student_detail',student_detail,name='student_detail'),
    path('create_student',create_student,name='create_student'),
    path('update_student',update_student,name='update_student'),
    path('delete_student',delete_student,name='delete_student'),
]
