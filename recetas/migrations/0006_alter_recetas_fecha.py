# Generated by Django 5.1.3 on 2024-11-25 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0005_alter_recetas_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='fecha',
            field=models.DateField(default=datetime.date(2024, 11, 25)),
        ),
    ]