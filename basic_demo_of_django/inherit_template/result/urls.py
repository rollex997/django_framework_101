from django.urls import path
from .views import *
urlpatterns = [
    path('',results,name="result"),
]
