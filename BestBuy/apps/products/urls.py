from os import name
from django.urls import path
from .views import home, DetailView


#app_name = 'products'

urlpatterns = [
    path('home/', home, name='home'),
    path('homee/', DetailView.as_view(), name='detailhome')
]
