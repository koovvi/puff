# Generated by Django 4.1.2 on 2023-01-01 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0023_alter_flower_description_alter_flower_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flower',
            old_name='photo',
            new_name='image',
        ),
    ]
