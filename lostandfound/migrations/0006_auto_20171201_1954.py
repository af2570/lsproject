# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostandfound', '0005_auto_20171201_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='time_lost',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
