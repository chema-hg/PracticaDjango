# Generated by Django 5.0 on 2024-01-21 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('valido_desde', models.DateTimeField()),
                ('valido_hasta', models.DateTimeField()),
                ('descuento', models.IntegerField(help_text='Valor del porcentaje (0-100)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('activo', models.BooleanField()),
            ],
        ),
    ]
