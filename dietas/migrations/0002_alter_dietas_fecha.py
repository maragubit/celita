# Generated by Django 5.1.3 on 2024-11-20 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietas',
            name='fecha',
            field=models.DateField(default=datetime.date(2024, 11, 20)),
        ),
    ]
