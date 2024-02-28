from django.urls import path
from pages.views_api import *
urlpatterns = [
    path('teams/',TeamAPIView.as_view(),name = 'teams'),
    path('teams_insert_update/',TeamAdmin.as_view(),name = 'teams_insert_update'),
    path('teams_delete/',TeamAdminDelete.as_view(),name = 'teams_delete'),
]

