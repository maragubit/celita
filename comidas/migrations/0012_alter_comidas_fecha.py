# Generated by Django 5.1.3 on 2024-11-25 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comidas', '0011_alter_comidas_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comidas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 11, 25, 17, 54, 55, 186709)),
        ),
    ]