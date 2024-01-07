from django.urls import path
from .views import *
urlpatterns = [
    path('', fees,name="fees"),
    path('fees_api', fees_api, name="fees_api")
]
