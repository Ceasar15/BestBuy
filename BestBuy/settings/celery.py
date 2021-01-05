import os
from celery import Celery 
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BestBuy.settings.base')

app = Celery('BestBuy')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)


