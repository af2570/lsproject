# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lostandfound', '0002_user_time_lost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id_lost',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='n_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nyu_email',
        ),
    ]
