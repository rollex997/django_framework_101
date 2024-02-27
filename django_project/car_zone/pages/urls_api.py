from django.urls import path
from pages.views_api import TeamAPIView
urlpatterns = [
    path('teams/',TeamAPIView.as_view(),name = 'teams')
]

