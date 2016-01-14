# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 05:21
from __future__ import unicode_literals

from django.db import migrations


def create_system_financial_account(apps, schema_editor):
    # We can't import the FinancialAccount model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    account = apps.get_model("crowdsourcing", "FinancialAccount")
    account.objects.get_or_create(is_system=True, type="paypal_deposit")


class Migration(migrations.Migration):
    dependencies = [
        ('crowdsourcing', '0011_auto_20151221_1618'),
    ]

    operations = [
        migrations.RunPython(create_system_financial_account),
    ]