from django.urls import path,include
urlpatterns = [
    path('auth_api/',include('auth_jwt.urls_api')),
]
