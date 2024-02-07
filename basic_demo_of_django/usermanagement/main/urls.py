from django.urls import path
from main.views import *
urlpatterns = [
    path('',main,name='main'),
    path('main_UID/<int:ID>',main_UID,name='main_UID'),
]
