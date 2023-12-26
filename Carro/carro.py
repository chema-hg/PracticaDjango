from django.conf import settings
from decimal import Decimal
from Tienda.models import Producto


class Carro:
    def __init__(self, request) -> None:
        """
        Inicializa el carro.
        """
        self.session = request.session
        # construimos un carro de la compra para esta sesión.
        carro = self.session.get(settings.CART_SESSION_ID)
        if not carro:
            # save an empty cart in the session
            carro = self.session[settings.CART_SESSION_ID] = {}
            # guardamos el carro en la sesión y va a ser un diccionario
            # con los productos que el usuario va a comprar
            # la clave es el id del producto y el valor son las características del producto
        self.carro = carro

    def agregar(self, producto, cantidad=1, override_cantidad=False):
        # Si el producto no esta en el carro
        producto_id = str(producto.id)
        if producto_id not in self.carro:
            self.carro[producto_id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 0,
                "imagen": producto.imagen.url,
            }
            # si el producto esta en el carro
            # solo sumamos la cantidad
        if override_cantidad:
            self.carro[producto_id]["cantidad"] = cantidad
        else:
            self.carro[producto_id]["cantidad"] += cantidad

        self.guardar_carro()

    def guardar_carro(self):
        self.session.modified = True

    def eliminar(self, producto):
        """
        Elimina el producto del carro.
        """
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()

    def restar_producto(self, producto):
        """
        Resta el producto del carro.
        """
        producto_id = str(producto.id)
        if producto_id in self.carro:
            self.carro[producto_id]["cantidad"] = (
                self.carro[producto_id]["cantidad"] - 1
            )
            if self.carro[producto_id]["cantidad"] < 1:
                self.eliminar(producto)
            self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True

    def __iter__(self):
        """
        Iterar sobre los artículos en el carrito y obtener los productos.
         de la base de datos.
        """
        product_ids = self.carro.keys()
        # Obtener los productos y añadirlos al carro
        products = Producto.objects.filter(id__in=product_ids)
        carro = self.carro.copy()
        for product in products:
            carro[str(product.id)]["producto"] = product
        for item in carro.values():
            item["precio"] = Decimal(item["precio"])
            item["precio_total"] = item["precio"] * item["cantidad"]
            yield item

    def __len__(self):
        """
        Cuenta todos los elementos del carro.
        """
        return sum(item["cantidad"] for item in self.carro.values())

    def get_total_price(self):
        return sum(
            Decimal(item["precio"]) * item["cantidad"] for item in self.carro.values()
        )

    def clear(self):
        """
         elimina el carro de la sesión.
        """
        del self.session[settings.CART_SESSION_ID]
        self.guardar_carro()