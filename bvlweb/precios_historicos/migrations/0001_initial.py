# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Precio_Historico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('maxima', models.DecimalField(max_digits=12, decimal_places=2)),
                ('minima', models.DecimalField(max_digits=12, decimal_places=2)),
                ('promedio', models.DecimalField(max_digits=12, decimal_places=2)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
