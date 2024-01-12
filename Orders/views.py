from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from Carro.carro import Carro
# Crea una tarea asincronica al finalizar la orden
from .tasks import order_created
# Para la gestion de la pasarela de pago
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.


def order_create(request):
    carro = Carro(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
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
