import os

from celery import Celery


# Set the default settings module so that we don't need to pass it to celery cli
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery('worker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()