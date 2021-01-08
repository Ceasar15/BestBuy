from django.http import request
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from .models import OrderItem
from .forms import OrderCreateForm
from apps.cart.cart import Cart
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                #clear the cart
                cart.clear()
                template = 'orders/order/created.html'
                context = {
                    'order': order,
                }
                # Lauch asynchronous task
                order_created.delay(order.id)
                return render(request, template, context)
    else:
        form = OrderCreateForm()
    template = 'orders/order/create.html'
    context = {
        'cart': cart,
        'form': form,
    }
    return render(request, template, context)


