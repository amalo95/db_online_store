# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_store', '0001_initial'),
        ('accounts', '0002_auto_20151203_0410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quaintity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(to='main_store.Product')),
                ('user', models.ForeignKey(to='accounts.UserProfile')),
            ],
        ),
    ]
