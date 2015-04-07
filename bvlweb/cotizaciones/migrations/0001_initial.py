# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monedas', '0001_initial'),
        ('propuestas', '0001_initial'),
        ('precios_historicos', '0001_initial'),
        ('negociaciones', '0001_initial'),
        ('precios_diarios', '0001_initial'),
        ('acciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('accion', models.ForeignKey(to='acciones.Accion')),
                ('moneda', models.ForeignKey(to='monedas.Moneda')),
                ('negociacion', models.OneToOneField(to='negociaciones.Negociacion')),
                ('precio_diario', models.OneToOneField(to='precios_diarios.Precio_Diario')),
                ('precio_historico', models.OneToOneField(blank=True, to='precios_historicos.Precio_Historico')),
                ('propuesta', models.OneToOneField(to='propuestas.Propuesta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='cotizacion',
            unique_together=set([('fecha', 'accion', 'precio_diario', 'propuesta', 'negociacion')]),
        ),
    ]
