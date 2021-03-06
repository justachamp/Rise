# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0038_auto_20150819_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='max_seats_chairman',
            field=models.PositiveIntegerField(help_text=b'How many seats may be reserved for Chairman users', null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='max_seats_executive',
            field=models.PositiveIntegerField(help_text=b'How many seats may be reserved for Executive users', null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='max_seats_express',
            field=models.PositiveIntegerField(help_text=b'How many seats may be reserved for Express users', null=True),
        ),
    ]
