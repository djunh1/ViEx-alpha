# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viex', '0002_auto_20151231_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stockData',
            field=models.ForeignKey(null=True, to='viex.StockData', default=None),
        ),
    ]
