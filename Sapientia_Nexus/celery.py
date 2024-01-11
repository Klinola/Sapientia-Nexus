import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sapientia_Nexus.settings')

app = Celery('Sapientia_Nexus')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()