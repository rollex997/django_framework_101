from django.urls import path
from api_view.views import *
urlpatterns = [
    path('create_update_data',create_update_data,name='create_update_data'),
    path('read_all_one_data',read_all_one_data,name='read_all_one_data'),
    path('delete_data',delete_data,name='delete_data'),
]
