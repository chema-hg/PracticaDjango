from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from Orders.models import Order


@shared_task
def payment_completed(order_id):
    """
    Tarea que envia una notificación por email cuando el 
    pedido ha sido pagado con exito.
    """
    order = Order.objects.get(id=order_id)
    # crea la factura por email
    subject = f'Unikgame - Factura no. {order.id}'
    message = 'Te enviamos la factura de tu compra en el archivo adjunto.'
    email = EmailMessage(subject,
                         message,
                         'admin@unikgame.com',
                         [order.email])
    # genera el PDF
    html = render_to_string('Orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(
        settings.STATIC_ROOT / 'Proyecto_web_app/css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out,
                                           stylesheets=stylesheets)
    # adjunta el archivo PDF a la notificación
    email.attach(f'order_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')
    # send e-mail
    email.send()
