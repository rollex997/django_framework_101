from django.urls import path,include
from auth_api.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('studentapi', StudentModelViewSet, basename='StudentModelViewSet')
urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'),name='auth_user')
]
