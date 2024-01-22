from django.urls import path
from result.views import *
urlpatterns = [
    path('', result,name='result'),
    path('insert_marks', insert_marks,name='insert_marks'),
    path('get_marks', get_marks,name='get_marks'),
    path('update_marks', update_marks,name='update_marks'),
    path('delete_marks', delete_marks,name='delete_marks'),
]
