from django.urls import path
from django.conf.urls import url

from . import views


#app_name = 'products'

urlpatterns = [

    path('catalog/', views.CatalogView.as_view(), name='products_catalog'),
    path('recom/', views.recom_list_view, name='recom_products'),
    path('gallery/', views.GalleryView.as_view(), name='products_gallery'),
#    url(r'^$', views.ProductListView.as_view(), name='products_list'),
    path('products/', views.product_list_view, name='products_list'),
    path('tag/<slug:tag_slug>/', views.product_list_view, name='product_list_by_tag'),
    path('filter/<slug:cat_filter>/', views.product_list_view, name="product_list_by_filter"),
    path('products/<int:id>/<slug:slug>/', views.product_detail_view),
#    path('<slug:slug>/', views.ProductDetailSlugView.as_view()),
]
