class Carro:
    def __init__(self, request) -> None:
        # almacenamos la request en una variable
        self.request = request
        #  aseguramos que el usuario este autenticado
        self.session = request.session
        # construimos un carro de la compra para esta sesión.
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
            # guardamos el carro en la sesión y va a ser un diccionario 
            # con los productos que el usuario va a comprar
            # la clave es el id del producto y el valor son las características del producto
        self.carro = carro
    
    def agregar(self, producto):
        # Si el producto no esta en el carro
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
            # si el producto esta en el carro
            # solo sumamos la cantidad
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    # si ya encontrado el producto corta el bucle.
                    break
        # Construiremos una función que guarde las modificaciones en el carro si hay una variación.
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True
    
    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()
    
    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
            

