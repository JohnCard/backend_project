# Generated by Django 4.1.1 on 2024-08-13 18:33

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('slug', models.SlugField(unique=True)),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(default=450)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]