# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-31 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0085_auto_20160331_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerconfig',
            name='phase_changed',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]