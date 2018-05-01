# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-01 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import pyfreebilling.rate.models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0002_auto_20180430_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customercountryrate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='customercountrytyperate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='customerdefaultrate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='customerdestinationrate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='customerprefixrate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='customerratecard',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='customerregionrate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='customerregiontyperate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='providercountryrate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='providercountrytyperate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='providerdefaultrate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='providerdestinationrate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='providerprefixrate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='providerratecard',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='providerregionrate',
            name='date_validity',
        ),
        migrations.RemoveField(
            model_name='providerregiontyperate',
            name='date_validity',
        ),
        migrations.AddField(
            model_name='customerratecard',
            name='date_end',
            field=models.DateTimeField(default=pyfreebilling.rate.models.default_time),
        ),
        migrations.AddField(
            model_name='customerratecard',
            name='date_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='providerratecard',
            name='date_end',
            field=models.DateTimeField(default=pyfreebilling.rate.models.default_time),
        ),
        migrations.AddField(
            model_name='providerratecard',
            name='date_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='providerratecard',
            name='provider_prefix',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]