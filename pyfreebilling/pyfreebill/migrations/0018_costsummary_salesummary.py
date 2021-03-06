# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-07 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyfreebill', '0017_sofiagateway_transport'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Cost Summary',
                'proxy': True,
                'verbose_name_plural': 'Cost Summary',
                'indexes': [],
            },
            bases=('pyfreebill.dimproviderdestination',),
        ),
        migrations.CreateModel(
            name='SaleSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Sale Summary',
                'proxy': True,
                'verbose_name_plural': 'Sales Summary',
                'indexes': [],
            },
            bases=('pyfreebill.dimcustomerdestination',),
        ),
    ]
