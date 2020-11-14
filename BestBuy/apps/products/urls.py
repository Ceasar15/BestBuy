from django.urls import path
from .views import home


#app_name = 'products'

urlpatterns = [
    path('home/', home, name='home'),
]
