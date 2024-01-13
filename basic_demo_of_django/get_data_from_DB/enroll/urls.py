from django.urls import path
from .views import *
urlpatterns = [
    path('',enroll,name="enroll"),
    path('get_all_data_api',get_all_data_api,name="get_all_data_api"),
]
