# Generated by Django 4.2.5 on 2023-12-24 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='update',
            new_name='updated',
        ),
    ]