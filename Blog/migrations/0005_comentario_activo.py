# Generated by Django 4.2.5 on 2023-11-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]