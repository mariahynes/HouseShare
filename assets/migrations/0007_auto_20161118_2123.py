# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20161015_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset_user_mapping',
            name='asset_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='the_asset', to='assets.Asset'),
        ),
    ]
