from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

#set default django settings module for 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jwt_practice.settings')

#create a celery instance
app = Celery('jwt_practice')

#load task modules from all registered Django app config
app.config_from_object('django.conf:settings',namespace='CELERY')

#Auto-Discover tasks in all Django applications
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request:{0!r}'.format(self.request))