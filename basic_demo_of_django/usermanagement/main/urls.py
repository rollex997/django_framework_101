from django.urls import path
from main.views import *
urlpatterns = [
    path('',main,name='main'),
]
