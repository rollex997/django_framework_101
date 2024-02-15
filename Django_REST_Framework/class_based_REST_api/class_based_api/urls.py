from django.urls import path
from class_based_api.views import StudentAPI

urlpatterns = [
    path('student_api', StudentAPI.as_view(), name='student_api'),
]
