# Generated by Django 4.1.7 on 2023-04-07 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0013_rename_cantidad_detalle_cantidad"),
    ]

    operations = [
        migrations.CreateModel(
            name="Historial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dia", models.DateTimeField(auto_now_add=True)),
                ("ganancias", models.FloatField(default=0.0)),
                ("ventas", models.IntegerField(default=0)),
            ],
        ),
    ]
