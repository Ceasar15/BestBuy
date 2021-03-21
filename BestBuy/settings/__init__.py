import django 
django.setup()


from .base import *
import os

env_name = os.getenv('ENV_NAME', 'development')

if env_name == 'production':
    from .production import *
else:
    from .development import *



