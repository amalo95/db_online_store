# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_cart_agg_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='agg_price',
            field=models.FloatField(),
        ),
    ]
