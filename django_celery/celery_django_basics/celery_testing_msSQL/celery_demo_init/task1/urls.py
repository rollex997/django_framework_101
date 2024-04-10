from django.urls import path
from task1.views import *
urlpatterns = [
    path('',StudentAPI.as_view(),name="StudentAPI"),
    path('SendEmail/',SendEmail.as_view(),name='SendEmail'),
]