# Generated by Django 4.1.2 on 2023-01-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0020_remove_flower_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]