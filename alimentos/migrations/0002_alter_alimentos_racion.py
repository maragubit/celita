# Generated by Django 5.1.3 on 2024-12-09 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimentos',
            name='racion',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
