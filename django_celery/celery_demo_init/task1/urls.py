from django.urls import path
from task1.views import *
urlpatterns = [
    path('',StudentDashboardView.as_view(),name="StudentDashboardView"),
    path('StudentDetailsView/',StudentDetailsView.as_view(),name="StudentDetailsView"),
    path('StudentAPI/',StudentAPI.as_view(),name="StudentAPI"),
]