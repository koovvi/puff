# Generated by Django 4.1.2 on 2023-01-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0026_alter_client_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_adress',
            field=models.CharField(max_length=255, verbose_name='Адрес'),
        ),
    ]
