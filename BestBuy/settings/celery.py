import os
from celery import Celery 
import django.conf

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BestBuy.settings.development')

app = Celery('BestBuy')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(django.conf.settings.INSTALLED_APPS)


