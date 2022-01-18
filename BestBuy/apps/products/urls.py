from django.urls import path

from . import views


app_name = 'products'

urlpatterns = [

    path('catalog/', views.CatalogView.as_view(), name='products_catalog'),
    path('recom/', views.recom_list_view, name='recom_products'),
    path('gallery/', views.GalleryView.as_view(), name='products_gallery'),
    path('products/', views.product_list_view, name='products_list'),
    path('tag/<slug:tag_slug>/', views.product_list_view, name='product_list_by_tag'),
    path('filter/<slug:cat_filter>/', views.product_list_view, name="product_list_by_filter"),
    path('filter_by_manufacturer/<slug:manu_filter>/', views.product_list_view, name="product_list_by_manufacturer_filter"),
    path('filter_by_name_ascend/<slug:name_ascend>/', views.product_list_view, name="products_list_by_name_ascend"),
    path('filter_by_name_descend/<slug:name_descend>/', views.product_list_view, name="products_list_by_name_descend"),
    path('filter_by_price_ascend/<slug:price_ascend>/', views.product_list_view, name="products_list_by_price_ascend"),
    path('filter_by_price_descend/<slug:price_descend>/', views.product_list_view, name="products_list_by_price_descend"),
    path('products/<int:id>/<slug:slug>/', views.product_detail_view, name="product_list_detail"),
#    path('<slug:slug>/', views.ProductDetailSlugView.as_view()),
]
