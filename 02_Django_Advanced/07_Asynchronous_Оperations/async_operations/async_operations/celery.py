from __future__ import unicode_literals, absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async_operations.settings')

app = Celery('async_operations')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

