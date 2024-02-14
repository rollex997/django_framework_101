from django.urls import path
from api.views import *
urlpatterns = [
    path('create_student',create_student,name='create_student'),
    path('update_student',update_student,name='update_student'),
    path('get_all_student',get_all_student,name='get_all_student'),
    path('get_one_student',get_one_student,name='get_one_student'),
    path('delete_student',delete_student,name='delete_student'),
]
