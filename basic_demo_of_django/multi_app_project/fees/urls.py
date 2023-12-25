from django.urls import path
from .views import *
urlpatterns = [
    path('fees', fees, name="fees"),
]
