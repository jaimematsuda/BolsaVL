# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precios_diarios', '0003_auto_20150407_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precio_diario',
            name='anterior',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='precio_diario',
            name='anterior_fecha',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
