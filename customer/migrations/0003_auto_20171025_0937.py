# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20171025_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='account_no',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Initial Deposit'),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(default='India', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pin_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='street',
            field=models.CharField(max_length=200, null=True),
        ),
    ]