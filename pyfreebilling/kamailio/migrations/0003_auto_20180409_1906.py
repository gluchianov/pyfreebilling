# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-09 17:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kamailio', '0002_auto_20180406_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='cfags',
            new_name='cflags',
        ),
    ]
