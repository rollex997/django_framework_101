
from token_app.views import *
from django.urls import path,include
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('studentapi/',StudentModelViewSet.as_view(),name='studentapi'),
]
