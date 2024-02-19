from django.urls import path
from home.views import *
urlpatterns = [
    path('',homepage,name='homepage'),
    path('empWorkCreate',empWorkCreate,name='empWorkCreate'),
    path('empWorkRead',empWorkRead,name='empWorkRead'),
    path('empEdit',empEdit,name='empEdit'),
    path('empdelete',empdelete,name='empdelete'),
]
