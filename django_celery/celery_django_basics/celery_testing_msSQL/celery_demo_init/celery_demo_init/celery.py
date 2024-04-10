from __future__ import absolute_import , unicode_literals
import os
from celery import Celery

#set the default django settings module for 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery_demo_init.settings')

#create a celery instance
app = Celery('celery_demo_init')

#load task modules from all registered Django app configs
app.config_from_object('django.conf:settings',namespace = 'CELERY')

# Auto-Discover tasks in all django applications
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request:{0!r}'.format(self.request))