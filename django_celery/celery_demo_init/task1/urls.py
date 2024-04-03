from django.urls import path
from task1.views import *
urlpatterns = [
    path('',StudentDashboardView.as_view(),name="StudentDashboardView"),
    path('StudentDetailsView/',StudentDetailsView.as_view(),name="StudentDetailsView"),
    path('StudentAPI/',StudentAPI.as_view(),name="StudentAPI"),
    path('StudentAPI/<int:student_id>/',StudentAPI.as_view(),name="StudentAPI_get_one_record"),
    
    path('StudentCategoryPage/',StudentCategoryPage.as_view(),name="StudentCategoryPage"),
    path('StudentCategoryAPI/',StudentCategoryAPI.as_view(),name="StudentCategoryAPI"),
]
