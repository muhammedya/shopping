# Generated by Django 3.2.11 on 2022-03-28 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopingapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='description',
        ),
    ]
