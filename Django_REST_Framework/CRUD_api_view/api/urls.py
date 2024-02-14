from django.urls import path
from api.views import *
urlpatterns = [
    path('create_update_student',create_update_student,name="create_update_student"),
    path('get_one_all_student',get_one_all_student,name="get_one_all_student"),
    path('delete_student',delete_student,name="delete_student"),
]
