from django.urls import path
from mixin_api.views import *
urlpatterns = [
    path('StudentListCreate',StudentListCreate.as_view(),name='StudentListCreate'),
    path('StudentUpdateRetireveDelete/<int:pk>',StudentUpdateRetireveDelete.as_view(),name='StudentUpdateRetireveDelete'),
]
