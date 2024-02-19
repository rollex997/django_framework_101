from django.urls import path
from home.views_api import *
urlpatterns = [
    path('homepage_api',homepage_api,name='homepage_api'),
]