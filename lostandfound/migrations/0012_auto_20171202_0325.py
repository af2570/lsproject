# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostandfound', '0011_auto_20171202_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostnyuid',
            name='time_lost',
            field=models.TimeField(auto_now_add=True, primary_key=True, serialize=False),
        ),
    ]
