# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-10 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_users', '0003_auto_20190510_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissioninfo',
            name='city',
            field=models.CharField(blank=True, max_length=50, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='admissioninfo',
            name='line',
            field=models.CharField(blank=True, max_length=255, verbose_name='xxx'),
        ),
        migrations.AlterField(
            model_name='admissioninfo',
            name='zip_code',
            field=models.IntegerField(blank=True, verbose_name='邮编'),
        ),
    ]
