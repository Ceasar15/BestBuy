from django.http import request
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.


def home(request):
    template = 'home.html'
    return render(request, template)

def contact(request):
    template = 'contact.html'
    return render(request, template)