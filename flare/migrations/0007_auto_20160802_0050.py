# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-01 19:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flare', '0006_auto_20160802_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='timestamp',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 8, 1, 19, 20, 7, 386000, tzinfo=utc)),
        ),
    ]