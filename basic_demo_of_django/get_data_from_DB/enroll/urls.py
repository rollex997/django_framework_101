from django.urls import path
from .views import *
urlpatterns = [
    path('',enroll,name="enroll"),
    path('enroll_api',enroll_api,name="enroll_api"),
]
