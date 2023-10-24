from django.contrib import admin

# Register your models here.

# Importar del modelo tanto la categoría como el post
from .models import Categoria, Post

class Categoria_Admin(admin.ModelAdmin):
    # Campos de solo lectura en el panel de administración.
    readonly_fields = ('created', 'updated')

@admin.register(Post)
class Post_Admin(admin.ModelAdmin):
    # Campos de solo lectura en el panel de administración.
    readonly_fields = ('created', 'updated')
    list_display = ['titulo', 'autor', 'created', 'updated']
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}
    raw_id_fields = ['autor']
    date_hierarchy = 'updated'
    ordering = ['updated', 'created']

# Registramos todo lo anterior.
admin.site.register(Categoria, Categoria_Admin)
