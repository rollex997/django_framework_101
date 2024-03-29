from django.urls import path
from task1.views import *
urlpatterns = [
    path('',StudentView.as_view(),name="StudentView"),
    path('StudentAPI/',StudentAPI.as_view(),name="StudentAPI"),
]