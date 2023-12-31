# Generated by Django 4.2.2 on 2023-06-29 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_venta_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='descuento',
            fields=[
                ('idDescuento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreDescuento', models.CharField(max_length=20)),
                ('cantidadDescuento', models.IntegerField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 1, 54, 26, 57544)),
        ),
    ]
