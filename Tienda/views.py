from django.shortcuts import render

# Como trabajamos con productos vamos a importarlos
from Tienda.models import Producto

# Create your views here.

def tienda(request):
    # productos = Producto.objects.all()
    productos = Producto.objects.filter(stock=True)
    # carga en la variable productos todos los juegos que hayamos introducido a través
    # del panel de administración de Django.
    contexto = {
        "productos": productos
    }
    
    return render(request, "Tienda/tienda.html", contexto)   
