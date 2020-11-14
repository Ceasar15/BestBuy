from django.http import request
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.


def home(request):
    template = 'products/home.html'
    return render(request, template)



class CategoryListView(ListView):
    template_name = 'products/home.html'


