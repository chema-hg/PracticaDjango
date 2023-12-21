from django.contrib import admin

from .models import *

# Register your models here.


class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "slug"]
    prepopulated_fields = {"slug": ("nombre",)}


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "slug", "precio", "stock", "created", "updated"]
    list_filter = ["stock", "created", "updated"]
    list_editable = ["precio", "stock"]
    prepopulated_fields = {"slug": ("nombre",)}

# Registramos ambas tablas y clases
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
