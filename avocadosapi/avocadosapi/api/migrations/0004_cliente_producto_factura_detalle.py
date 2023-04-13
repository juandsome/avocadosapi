# Generated by Django 4.1.7 on 2023-03-30 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_usuario_rol"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                ("nombre", models.TextField(default="nombre", max_length=30)),
                ("cedula", models.TextField(default="cedula", max_length=10)),
                ("direccion", models.TextField(default="direccion", max_length=50)),
                ("telefono", models.TextField(default="telefono", max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
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
                ("nombre", models.TextField(default="nombre", max_length=100)),
                ("precio", models.FloatField(default=0.0, max_length=20)),
                ("stock", models.IntegerField(default=0, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Factura",
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
                ("fecha", models.DateTimeField(auto_now_add=True)),
                (
                    "Cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.cliente"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Detalle",
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
                ("Precio", models.FloatField(default=0.0, max_length=20)),
                (
                    "Factura",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.factura"
                    ),
                ),
                (
                    "Producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.producto"
                    ),
                ),
            ],
        ),
    ]