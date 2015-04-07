# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0003_auto_20150402_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='precio_historico',
            field=models.OneToOneField(null=True, blank=True, to='precios_historicos.Precio_Historico'),
            preserve_default=True,
        ),
    ]
