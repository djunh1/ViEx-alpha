# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viex', '0008_auto_20160101_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stockData',
            field=models.ForeignKey(to='viex.StockData', null=True),
        ),
    ]
