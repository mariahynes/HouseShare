# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_booking_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
