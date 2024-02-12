from django.urls import path
from API.views import *
urlpatterns = [
    path('student_detail/<int:Student_ID>',student_detail,name="student_detail"),
    path('',student_list,name="student_list"),
]
