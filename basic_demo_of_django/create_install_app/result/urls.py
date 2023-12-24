from django.urls import path
from .views import *
urlpatterns = [
    path('result',result, name="result"),
]
