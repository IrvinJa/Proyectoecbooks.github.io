# Generated by Django 4.2.6 on 2023-11-23 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementocarrito',
            name='carrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elementoscarrito_set', to='carrito.carrito'),
        ),
    ]
