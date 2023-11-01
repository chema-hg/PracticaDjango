from django.contrib import admin

# Register your models here.

# Importar del modelo tanto la categoría como el post
from .models import Categoria, Post, Comentario

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

@admin.register(Comentario)
class Comentario_admin(admin.ModelAdmin):
    list_display = ['autor', 'email', 'post', 'created', 'activo']
    list_filter = ['activo', 'created', 'updated']
    search_fields = ['autor', 'email', 'cuerpo']

# Registramos el modelo Categoria. (ya que se puede hacer asi o con un decorador como
# los otros modelos)
admin.site.register(Categoria, Categoria_Admin)

