# Generated by Django 4.2.11 on 2024-04-29 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=9, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50, unique=True)),
                ('marca', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('fecha_adquisicion', models.DateField()),
                ('fecha_instalacion', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Orden_De_fabricacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_fabricacion', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Orden de fabricacion',
                'verbose_name_plural': 'Ordenes de fabricacion',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_proceso', models.CharField(max_length=10, unique=True)),
                ('nombre_proceso', models.CharField(max_length=50)),
                ('referencia', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('empleado_asignados', models.ManyToManyField(to='appGestionProduccion.empleado')),
                ('equipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appGestionProduccion.equipo')),
                ('referencia_de_fabricacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appGestionProduccion.orden_de_fabricacion')),
            ],
            options={
                'verbose_name': 'Proceso',
                'verbose_name_plural': 'Procesos',
                'ordering': ['-created'],
            },
        ),
    ]
