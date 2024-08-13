# Generated by Django 4.1.1 on 2024-08-13 18:32

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Prducto nuevo', max_length=100)),
                ('price', models.FloatField(default=100)),
                ('description', models.CharField(default='On sale', max_length=100)),
                ('color', colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None)),
                ('slug', models.SlugField(blank=True, default='new-product')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('credit_card', models.JSONField()),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]