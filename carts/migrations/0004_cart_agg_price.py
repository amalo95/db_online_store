# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cart_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='agg_price',
            field=models.DecimalField(default=1.99, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
