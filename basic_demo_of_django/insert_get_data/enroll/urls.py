from django.urls import path
from enroll.views import *
urlpatterns = [
    path('',enroll,name="enroll"),
    path('insert_data',insert_data,name='insert_data'),
    path('get_data',get_data,name='get_data'),
    path('update_data',update_data,name='update_data'),
    path('delete_data',delete_data,name="delete_data"),
]
