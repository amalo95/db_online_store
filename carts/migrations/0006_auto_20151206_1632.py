# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20151206_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='agg_price',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
