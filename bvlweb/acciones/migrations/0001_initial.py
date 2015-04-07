# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('nemonicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('empresa', models.ForeignKey(to='empresas.Empresa')),
                ('nemonico', models.OneToOneField(to='nemonicos.Nemonico')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='accion',
            unique_together=set([('empresa', 'nemonico')]),
        ),
    ]
