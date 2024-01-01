from django.urls import path
from .views import *
urlpatterns = [
    path('course', course, name='course'),
]
