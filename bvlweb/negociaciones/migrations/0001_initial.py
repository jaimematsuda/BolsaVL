# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Negociacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cant_accion', models.PositiveIntegerField()),
                ('cant_operacion', models.PositiveIntegerField()),
                ('variacion', models.DecimalField(max_digits=12, decimal_places=2)),
                ('monto_negociado', models.DecimalField(max_digits=12, decimal_places=2)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
