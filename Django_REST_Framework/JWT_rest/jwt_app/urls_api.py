from jwt_app.views_api import *
from django.urls import path,include
from rest_framework.routers import DefaultRouter
#JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView
router = DefaultRouter()
router.register('studentapi', StudentModelViewSet, basename='StudentModelViewSet')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'),name='auth_user'),
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refreshtoken'),
    path('verifytoken/',TokenVerifyView.as_view(),name='verifytoken'),
]
