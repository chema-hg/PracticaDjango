# Generated by Django 4.2.5 on 2023-10-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(blank=True, null=True, to='Blog.categoria'),
        ),
    ]