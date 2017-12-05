# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostandfound', '0010_auto_20171202_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='lostNYUID',
            fields=[
                ('net_id', models.CharField(max_length=10, verbose_name='Net ID')),
                ('time_lost', models.DateTimeField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]