# Generated by Django 4.2.5 on 2023-12-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0005_producto_slug_alter_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['nombre'], 'verbose_name': 'producto', 'verbose_name_plural': 'productos'},
        ),
        migrations.AddIndex(
            model_name='producto',
            index=models.Index(fields=['id', 'slug'], name='Tienda_prod_id_c93c59_idx'),
        ),
        migrations.AddIndex(
            model_name='producto',
            index=models.Index(fields=['nombre'], name='Tienda_prod_nombre_fe54c1_idx'),
        ),
        migrations.AddIndex(
            model_name='producto',
            index=models.Index(fields=['-created'], name='Tienda_prod_created_b9ad5d_idx'),
        ),
    ]
