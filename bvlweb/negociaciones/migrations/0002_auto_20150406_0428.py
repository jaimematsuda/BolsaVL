# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negociaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negociacion',
            name='cant_accion',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='negociacion',
            name='cant_operacion',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
