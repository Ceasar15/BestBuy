# from django.core.mail.message import EmailMessage
# from .models import Order
# from BestBuy.settings.celery import app

# @app.task()
# def order_created(order_id):
#     order = Order.objects.get(id=order_id)
#     subjectHead = f"Order Details No. {order.id}"
#     message = f'Dear {order.first_name}, \n\n' \
#         f'You have successfully placed an order.' \
#         f'Your order ID is {order.id}.'
            
#     email = EmailMessage (
#         subject=subjectHead,
#         body=message,
#         from_email='ceasarkwadwo@gmail.com',
#         to=[order.email,]
#     )
#     email.send()
#     return email
