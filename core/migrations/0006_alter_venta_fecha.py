# Generated by Django 4.2.2 on 2023-07-03 02:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_descuento_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 2, 22, 58, 54, 98346)),
        ),
    ]
