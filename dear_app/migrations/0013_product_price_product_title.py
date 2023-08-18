# Generated by Django 4.2 on 2023-06-07 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dear_app', '0012_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
