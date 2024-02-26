from django.urls import path, include
from pages.views import *
urlpatterns = [
    path('',homepage,name='homepage'),
    path('about/',about_page,name='aboutpage'),
    path('services/',services_page,name='servicespage'),
    path('contact/',contact_page,name='contactpage'),
]
