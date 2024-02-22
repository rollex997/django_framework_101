
from token_app.views import *
from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from token_app.auth import CustomAuthToken
router = DefaultRouter()
router.register('studentapi', StudentModelViewSet, basename='StudentModelViewSet')
urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'),name='auth_user'),
    path('gettoken/',CustomAuthToken.as_view())
]
