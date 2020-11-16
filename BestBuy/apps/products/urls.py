from os import name
from django.urls import path
from . import views


#app_name = 'products'

urlpatterns = [

    path('catalog/', views.CatalogView.as_view(), name='products_catalog'),
    path('gallery/', views.GalleryView.as_view(), name='products_gallery')
]
