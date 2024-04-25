from django.urls import include, path
from auth_jwt.views_api import *
from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
   TokenVerifyView,
)


urlpatterns = [
  
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


   path('UserRoleList/',UserRoleList.as_view(),name="UserRoleList"),
   path('RegisterUser/',RegisterUser.as_view(),name="RegisterUser"),
   path('EmailVerification/',EmailVerification.as_view(),name="EmailVerification"),
   path('LogoutView/',LogoutView.as_view(),name="LogoutView"),
   path('homeView/',homeView.as_view(),name="homeView"),
]

