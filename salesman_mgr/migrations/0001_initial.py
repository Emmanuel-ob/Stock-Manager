# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-01 14:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=40)),
                ('itemCode', models.CharField(max_length=40)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_restocked', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
