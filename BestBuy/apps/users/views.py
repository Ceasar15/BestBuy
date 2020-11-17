from django.shortcuts import render
from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def sign_up(request):
    template = 'users/signup.html'
    return render(request, template )

def login(request):
    template = 'users/login.html'
    return render(request, template)

