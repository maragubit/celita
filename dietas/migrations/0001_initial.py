# Generated by Django 5.1.3 on 2024-11-18 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dietas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField(default=datetime.date(2024, 11, 18))),
                ('desayuno', models.IntegerField()),
                ('media_manana', models.IntegerField(verbose_name='media mañana')),
                ('almuerzo', models.IntegerField()),
                ('merienda', models.IntegerField()),
                ('cena', models.IntegerField()),
                ('antes_dormir', models.IntegerField(verbose_name='antes de dormir')),
                ('observaciones', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
