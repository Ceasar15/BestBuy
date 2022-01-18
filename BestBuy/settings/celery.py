import os
from celery import Celery 
import django.conf

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BestBuy.settings.development')

app = Celery('BestBuy', backend='redis://127.0.0.1:5672/0' , broker='redis://localhost:5672/0')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(django.conf.settings.INSTALLED_APPS)


