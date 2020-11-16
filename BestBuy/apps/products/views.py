from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.


def home(request):
    template = 'home.html'
    return render(request, template)

def contact(request):
    template = 'contact.html'
    return render(request, template)

def faq(request):
    template = 'faq.html'
    return render(request, template)

class CatalogView(TemplateView):
    template_name = 'products/catalog.html'

class GalleryView(TemplateView):
    template_name = 'products/gallery.html'