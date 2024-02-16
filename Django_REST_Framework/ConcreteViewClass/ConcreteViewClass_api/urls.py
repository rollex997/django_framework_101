from django.urls import path
from ConcreteViewClass_api.views import *
urlpatterns = [
    path('StudentList',StudentList.as_view(),name='StudentList'),
    path('StudentRetrieve/<int:pk>',StudentRetrieve.as_view(),name='StudentRetrieve'),
    path('StudentCreate',StudentCreate.as_view(),name='StudentCreate'),
    path('StudentUpdate/<int:pk>',StudentUpdate.as_view(),name='StudentUpdate'),
    path('StudentDelete/<int:pk>',StudentDelete.as_view(),name='StudentDelete'),
]
