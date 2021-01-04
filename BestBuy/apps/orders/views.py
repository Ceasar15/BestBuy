from django.http import request
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from apps.cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                #clear the cart

# Create your views here.

