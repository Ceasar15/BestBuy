from os import name
from django.urls import path
from django.conf.urls import url

from . import views


#app_name = 'products'

urlpatterns = [

    path('catalog/', views.CatalogView.as_view(), name='products_catalog'),
    path('recom/', views.recom_list_view, name='recom_products'),
    path('gallery/', views.GalleryView.as_view(), name='products_gallery'),
#    url(r'^$', views.ProductListView.as_view(), name='products_list'),
    path('^$', views.product_list_view, name='products_list'),
    url(r'^(?P<slug>[\w-]+)/$', views.ProductDetailSlugView.as_view())
]
