from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    """
    Función para enviar una notificación por correo electrónico cuando se realiza un pedido
    correctamente.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Orden nº. {order.id}'
    message = f'Estimado {order.first_name},\n\n' \
              f'Su pedido ha sido realizado correctamente.' \
              f'Su ID del pedido es {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent