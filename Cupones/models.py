from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Cupon(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    valido_desde = models.DateTimeField()
    valido_hasta = models.DateTimeField()
    descuento = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], help_text='Valor del porcentaje (0-100)')
    activo = models.BooleanField()

    def __str__(self):
        return self.codigo
