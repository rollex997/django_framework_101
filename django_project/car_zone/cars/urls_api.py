from django.urls import path
from cars.views_api import *
urlpatterns = [
    path('cars/',Cars.as_view(),name='cars'),
    path('cars_insert_or_update/',CarAdmin.as_view(),name='cars_insert_or_update'),
    path('car_delete/',CarAdminDelete.as_view(),name='car_delete'),
    path('featured_cars/',FeaturedCars.as_view(),name='featured_cars'),
    path('latest_cars/',LatestCars.as_view(),name='latest_cars'),
]
