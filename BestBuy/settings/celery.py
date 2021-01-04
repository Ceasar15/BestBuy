import os
from celery import Celery 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

app = Celery('BestBuy')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(app)


