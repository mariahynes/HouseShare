# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_auto_20161119_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetail',
            name='booking_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookingdetails', to='bookings.Booking'),
        ),
    ]
