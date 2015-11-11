# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CazaRecompensa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'cazarecompensa',
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'foto_mascota',
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('raza', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'mascota',
            },
        ),
        migrations.CreateModel(
            name='MascotaEncontrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recompensa', models.CharField(max_length=20, blank=True)),
                ('fechaencontrado', models.DateTimeField(blank=True)),
                ('direccionencontrado', models.CharField(max_length=50, blank=True)),
                ('comentario', models.TextField()),
                ('mascota', models.ForeignKey(to='mascotas.Mascota')),
            ],
            options={
                'db_table': 'mascota_econtrada',
            },
        ),
        migrations.CreateModel(
            name='MascotaPerdida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recompensa', models.CharField(max_length=20, blank=True)),
                ('fechaperdido', models.DateTimeField()),
                ('direccionperdido', models.CharField(max_length=50)),
                ('comentario', models.TextField()),
                ('mascota', models.ForeignKey(to='mascotas.Mascota')),
            ],
            options={
                'db_table': 'mascota_perdida',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.AddField(
            model_name='mascota',
            name='usuario',
            field=models.ForeignKey(blank=True, to='mascotas.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='foto',
            name='mascota',
            field=models.ForeignKey(to='mascotas.Mascota'),
        ),
        migrations.AddField(
            model_name='cazarecompensa',
            name='mascota_encontrada',
            field=models.ForeignKey(to='mascotas.MascotaEncontrada'),
        ),
        migrations.AddField(
            model_name='cazarecompensa',
            name='usuario',
            field=models.ForeignKey(to='mascotas.Usuario'),
        ),
    ]
