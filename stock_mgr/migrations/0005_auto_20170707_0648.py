# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-07 05:48
from __future__ import unicode_literals

from django.db import migrations, models
import stock_mgr.models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_mgr', '0004_auto_20170612_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to=stock_mgr.models.get_upload_file_name),
        ),
    ]