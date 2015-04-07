# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propuestas', '0002_auto_20150406_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propuesta',
            name='compra',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='propuesta',
            name='venta',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True),
            preserve_default=True,
        ),
    ]
