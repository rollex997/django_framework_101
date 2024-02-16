from django.urls import path,include
from viewSet.views import *
from rest_framework.routers import DefaultRouter
#creating router object
router = DefaultRouter()
#register classes that inherit ViewSet using routers
router.register('StudentViewSet', StudentViewSet,basename='StudentViewSet')
urlpatterns = [
    path('',include(router.urls)),
]
