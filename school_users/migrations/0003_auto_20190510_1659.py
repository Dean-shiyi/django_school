# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-10 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_users', '0002_admissioninfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissioninfo',
            name='birth',
            field=models.DateField(blank=True, verbose_name='学生生日'),
        ),
        migrations.AlterField(
            model_name='admissioninfo',
            name='course',
            field=models.CharField(blank=True, max_length=50, verbose_name='选择课程'),
        ),
        migrations.AlterField(
            model_name='admissioninfo',
            name='course_time',
            field=models.CharField(blank=True, max_length=50, verbose_name='课程时间'),
        ),
        migrations.AlterField(
            model_name='admissioninfo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='学生邮箱'),
        ),
        migrations.AlterField(
            model_name='admissioninfo',
            name='gender',
            field=models.CharField(blank=True, max_length=10, verbose_name='学生性别'),
        ),
        migrations.AlterField(
            model_name='admissioninfo',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='学生姓名'),
        ),
        migrations.AlterField(
            model_name='admissioninfo',
            name='phone',
            field=models.CharField(blank=True, max_length=11, verbose_name='学生电话'),
        ),
    ]
