from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name="home"),
    path('course', course, name="course"),
    path('fees', fees, name="fees"),
    path('result', result, name="result"),
]
