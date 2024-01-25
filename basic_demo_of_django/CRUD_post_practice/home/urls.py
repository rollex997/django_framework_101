from django.urls import path
from home.views import *
urlpatterns = [
    path('',home,name='home'),
    path('recieve_data_from_student_app/<int:id>/',get_Id,name="recieve_data_from_student_app"),
    path('get_data_by_ID',get_data_by_ID,name='get_data_by_ID'),
]
