from django.urls import path
from home.views_api import *
urlpatterns = [
    path('homepage_api',homepage_api,name='homepage_api'),
    path('empWorkCreate_or_empWorkUpdate',empWorkCreate_or_empWorkUpdate,name='empWorkCreate_or_empWorkUpdate'),
    path('empReadAll_OR_one',empReadAll_OR_one,name='empReadAll_OR_one'),
    path('empDelete',empDelete,name='empDelete'),
]