# Generated by Django 5.1.3 on 2024-11-21 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comidas', '0004_alter_comidas_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comidas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 21, 16, 43, 19, 350426)),
        ),
    ]