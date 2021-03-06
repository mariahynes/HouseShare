# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 20:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '0004_auto_20161011_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset_user_mapping',
            name='inviter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_to_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]


# operations = [
#     migrations.AddField(
#         model_name='asset_user_mapping',
#         name='inviter',
#         field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='linked_to_owner',
#                                 to=settings.AUTH_USER_MODEL),
#     ),
# ]