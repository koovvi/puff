# Generated by Django 4.1.2 on 2023-01-01 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0024_rename_photo_flower_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='image',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Телефонный номер')),
                ('client_adress', models.CharField(max_length=255, verbose_name='Адресс')),
                ('client_flower', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articles.flower')),
            ],
        ),
    ]