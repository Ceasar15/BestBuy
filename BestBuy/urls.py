from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from apps.products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('apps.cart.urls', namespace='cart')),
    path('orders/', include('apps.orders.urls', namespace='orders') ),
    path('coupons/', include('apps.coupons.urls', namespace='coupons')),
    url('products/',include('apps.products.urls')),
    url('users/', include('apps.users.urls')),
    path('', views.home, name='home' ),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)