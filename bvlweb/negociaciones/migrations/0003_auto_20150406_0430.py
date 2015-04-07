# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negociaciones', '0002_auto_20150406_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negociacion',
            name='cant_accion',
            field=models.DecimalField(max_digits=12, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='negociacion',
            name='cant_operacion',
            field=models.DecimalField(max_digits=12, decimal_places=0),
            preserve_default=True,
        ),
    ]
