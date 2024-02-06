import redis
from django.conf import settings
from .models import Producto

# Conectamos a redis
r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)


class Recomendar:
    def obtener_key_producto(self, id):
        return f'producto:{id}:comprado_junto'

    def productos_comprados(self, productos):
        productos_ids = [p.id for p in productos]
        for producto_id in productos_ids:
            for junto_id in productos_ids:
                # obtenemos el otro producto comprado junto con este
                if producto_id != junto_id:
                    # incrementamos el contador de junto comprado
                    r.zincrby(self.obtener_key_producto(producto_id),
                              1, junto_id)

    def sugerir_productos(self, productos, max_resultados=6):
        productos_ids = [p.id for p in productos]
        if len(productos) == 1:
            # solamente hay un producto
            sugerencias = r.zrange(
                self.obtener_key_producto(productos_ids[0]),
                0, -1, desc=True)[:max_resultados]
        else:
            # generamos una clave temporal
            flat_ids = ''.join([str(id) for id in productos_ids])
            tmp_key = f'tmp_{flat_ids}'
            # multiples productos, combinamos las puntuaciones de los productos
            # guardamos el resultado ordenado en una clave temporal
            keys = [self.obtener_key_producto(id) for id in productos_ids]
            r.zunionstore(tmp_key, keys)
            # eliminamos los identificadores de los productos recomendados
            r.zrem(tmp_key, *productos_ids)
            # obtener los ID de los productos por su puntuación, ordenada de forma descendente
            sugerencias = r.zrange(tmp_key, 0, -1, desc=True)[:max_resultados]
            # removemos la clave temporal
            r.delete(tmp_key)
        productos_sugeridos_ids = [int(id) for id in sugerencias]
        # establecemos los productos sugeridos y los ordenamos por orden de aparición.
        productos_sugeridos = list(
            Producto.objects.filter(id__in=productos_sugeridos_ids))
        productos_sugeridos.sort(
            key=lambda x: productos_sugeridos_ids.index(x.id))
        return productos_sugeridos
    
    def limpiar_compras(self):
        for id in Producto.objects.values_list('id', flat=True):
            r.delete(self.obtener_key_producto(id))
