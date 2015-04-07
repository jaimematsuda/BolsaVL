# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monedas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneda',
            name='name',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
