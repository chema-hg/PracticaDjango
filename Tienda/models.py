from django.db import models

# Create your models here.

# Creamos dos modelos para la categoría del producto (tipo de consola)
# y para el producto (el juego en si).


class CategoriaProducto(models.Model):
    """Registrará las diferentes consolas para las que vendemos juegos"""

    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "categoriaProducto"
        verbose_name_plural = "categoriasProductos"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """Registra los propios juegos en si."""

    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(
        CategoriaProducto, on_delete=models.CASCADE, related_name="categoria_productos"
    )
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.BooleanField(default=True)
    # hay que tener instalado la libreria pillow para poder subir imagenes
    imagen = models.ImageField(upload_to="Tienda", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre
