from django.http import request
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
#import weasyprint

from .models import OrderItem, Order
from .forms import OrderCreateForm
from apps.cart.cart import Cart
from .tasks import order_created

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders//order/detail.html', {'order': order})

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


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    #weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response
