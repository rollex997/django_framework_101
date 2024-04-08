from django.urls import path
from task1.views import *
urlpatterns = [
    path('',StudentDashboardView.as_view(),name="StudentDashboardView"),
    path('StudentDetailsView/',StudentDetailsView.as_view(),name="StudentDetailsView"),
    path('StudentAPI/',StudentAPI.as_view(),name="StudentAPI"),
    path('StudentAPI/<int:student_id>/',StudentAPI.as_view(),name="StudentAPI_get_one_record"),
    
    path('StudentCategoryPage/',StudentCategoryPage.as_view(),name="StudentCategoryPage"),
    path('StudentCategoryAPI/',StudentCategoryAPI.as_view(),name="StudentCategoryAPI"),
    path('MarksCRUD_student_API/<int:student_id>/',MarksCRUD_student_API.as_view(),name="MarksCRUD_student_API"),

    #working (test)
    path('pdf_page_caller/<int:student_id>/<int:categoryId>/<int:marks_id>/', pdf_page_caller.as_view(), name="pdf_page_caller"),
    path('pdf_page/',pdf_page,name="pdf_page"),
]
