# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precios_diarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precio_diario',
            name='ex_derecho',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
