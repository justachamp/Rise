# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0025_auto_20150309_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='tax_percentage',
            field=models.DecimalField(default=Decimal('0.075'), max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
