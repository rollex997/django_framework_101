from django.urls import path,include
from api.views import *
from rest_framework.routers import DefaultRouter
#creating a router object
router=DefaultRouter()
router.register('singer',singerViewSet, basename='singer')
router.register('song',songViewSet, basename='song')
urlpatterns = [
    path('',include(router.urls)),
]
