# Generated by Django 4.2 on 2023-06-24 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dear_app', '0018_productsec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsec',
            name='seller',
        ),
    ]
