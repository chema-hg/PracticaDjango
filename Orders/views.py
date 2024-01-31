from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from Carro.carro import Carro
# Crea una tarea asincronica al finalizar la orden
from .tasks import order_created
# Para la gestion de la pasarela de pago
from django.urls import reverse
from django.shortcuts import redirect
# Para crear una vista personalizada en el panel de administración.
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Order

# Para renderizar el archivo PDF de las facturas.
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

# Create your views here.


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('Orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[
        weasyprint.CSS(settings.STATIC_ROOT / 'Proyecto_web_app/css/pdf.css')])
    return response


def order_create(request):
    carro = Carro(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if carro.cupon:
                order.cupon = carro.cupon
                order.descuento = carro.cupon.descuento
                order.save()
            for item in carro:
                OrderItem.objects.create(
                    order=order,
                    product=item["producto"],
                    price=item["precio"],
                    quantity=item["cantidad"],
                )
            # Limpia el carro
            carro.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            # return render(request, "Orders/order/created.html", {"order": order})
            order_created.delay(order.id)
            # guarda el pedido en la sesión
            request.session['order_id'] = order.id
            # redirecciona para hacer el pago
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request, "Orders/order/create.html", {"cart": carro, "form": form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/Orders/order/detail.html', {'order': order})
