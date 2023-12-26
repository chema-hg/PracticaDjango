from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from Carro.carro import Carro


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
            return render(request, "Orders/order/created.html", {"order": order})
    else:
        form = OrderCreateForm()
    return render(request, "Orders/order/create.html", {"cart": carro, "form": form})
