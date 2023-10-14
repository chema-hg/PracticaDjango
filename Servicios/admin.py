from django.contrib import admin

# importamos el modelo a registrar
from .models import Servicio

# # Register your models here.
# admin.site.register(Servicio)

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
