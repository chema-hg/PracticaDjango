from django.shortcuts import render

# Importamos la clase Carro
from .carro import Carro

# Importamos los productos
from Tienda.models import Producto

# cada vez que modifiquemos algo en el carrito tendra que reflejarse en la 
# pagina de la tienda por lo que tendremos que importar el redirect
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

# Create your views here.

# vista para agregar un producto al carro
@login_required
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    # agregamos el producto al carro
    carro.agregar(producto=producto)
    # redireccionamos a la tienda
    return redirect("Tienda:tienda")

# vista para eliminar un producto del carro
def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    # eliminamos el producto del carro
    carro.eliminar(producto=producto)
    # redireccionamos a la tienda
    return redirect("Tienda:tienda")

# restar un producto del carro
def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    # restamos el producto del carro
    carro.restar_producto(producto=producto)
    # redireccionamos a la tienda
    return redirect("Tienda:tienda")

# vista para limpiar el carro
def limpiar_carro(request):
    carro = Carro(request)
    # limpiamos el carro
    carro.limpiar_carro()
    # redireccionamos a la tienda
    return redirect("Tienda:tienda")

# vista para mostrar los productos del carro
def mostrar_carro(request):
    productos = Producto.objects.all()
    carro = Carro(request)
    contexto = {
        "productos": productos,
        "carro": carro
    }
    return render(request, "Tienda/carro_detalle.html", contexto)

