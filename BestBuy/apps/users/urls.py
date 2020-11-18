from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
 #   path('login/', views.login, name='login'),
    url(r"^", include("django.contrib.auth.urls")),
]
