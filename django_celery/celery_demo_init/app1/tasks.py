from __future__ import absolute_import , unicode_literals
#import shared tasks decorator
from celery import shared_task


#here we want to use shared tasks decorator
#create task without any concrete app instance
@shared_task
def add(x,y):
   return x+y