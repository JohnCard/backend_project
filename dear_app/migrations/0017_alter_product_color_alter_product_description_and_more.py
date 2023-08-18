# Generated by Django 4.2 on 2023-06-14 08:00

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dear_app', '0016_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='On sale', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_dimensions',
            field=models.TextField(default='[("Altura":20),("Anchura": 5),("Longitud": 8)]'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dear_app.market'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='new-product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(default='Prducto nuevo', max_length=100),
        ),
    ]
