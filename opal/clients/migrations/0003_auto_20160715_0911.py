# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-15 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20160714_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
