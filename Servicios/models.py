from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='Servicios')
    created = models.DateField(auto_now_add=True)
    # Para que automaticamente actualice las fechas usamos el argumento
    # auto_now_add = True para guardar la fecha de cuando se cree el registro
    updated = models.DateField(auto_now=True)
    # auto_now = True para guardar la fecha cuando se guarde o actualice el 
    # registro.

    class Meta:
        verbose_name = "Servicio Ofrecido"
        verbose_name_plural = "Servicios Ofrecidos"

    def __str__(self):
        return self.titulo
