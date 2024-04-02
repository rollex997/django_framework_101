from django.urls import path
from marks.views import * 
urlpatterns = [
    path('MarksPage/',MarksPage.as_view(),name="MarksPage"),
    path('MarksCRUD_API/',MarksCRUD_API.as_view(),name="MarksCRUD_API"),
]