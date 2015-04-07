# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negociaciones', '0004_auto_20150406_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negociacion',
            name='cant_accion',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='negociacion',
            name='cant_operacion',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='negociacion',
            name='monto_negociado',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
    ]
