# Generated by Django 4.1.5 on 2023-06-02 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_venta_detalle"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venta",
            name="fecha",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 2, 15, 39, 3, 908887)
            ),
        ),
    ]
