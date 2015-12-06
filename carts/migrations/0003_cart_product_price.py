# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20151204_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_price',
            field=models.DecimalField(default=1.99, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
