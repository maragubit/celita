# Generated by Django 5.1.3 on 2024-11-20 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comidas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comidas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 20, 13, 52, 27, 886027)),
        ),
    ]