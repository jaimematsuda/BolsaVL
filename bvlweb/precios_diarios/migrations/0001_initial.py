# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Precio_Diario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anterior_fecha', models.DateField()),
                ('anterior', models.DecimalField(max_digits=12, decimal_places=2)),
                ('apertura', models.DecimalField(max_digits=12, decimal_places=2)),
                ('cierre', models.DecimalField(max_digits=12, decimal_places=2)),
                ('ex_derecho', models.DecimalField(max_digits=12, decimal_places=2, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
