# Generated by Django 4.1.2 on 2023-01-01 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_alter_flower_image_client'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
    ]