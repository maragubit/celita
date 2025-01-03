# Generated by Django 5.1.3 on 2024-11-18 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recetas', to='recetas.recetas')),
            ],
        ),
    ]