from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'users'


urlpatterns = [
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),
 #   path('login/', views.login, name='login'),
    path('', include("django.contrib.auth.urls")),
]
