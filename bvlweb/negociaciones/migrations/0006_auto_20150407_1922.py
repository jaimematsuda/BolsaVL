# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negociaciones', '0005_auto_20150406_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negociacion',
            name='variacion',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
