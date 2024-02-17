from django.urls import path,include
from auth_api.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('studentapi', StudentModelViewSet, basename='StudentModelViewSet')
urlpatterns = [
    path('',include(router.urls))
]
