from django.urls import path
from django.conf.urls import url

from . import views


#app_name = 'products'

urlpatterns = [

    path('catalog/', views.CatalogView.as_view(), name='products_catalog'),
    path('gallery/', views.GalleryView.as_view(), name='products_gallery'),
    url(r'^$', views.ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', views.ProductDetailSlugView.as_view()),
]
