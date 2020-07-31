# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2020-06-10 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('sex', models.BooleanField(default=True, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
            ],
        ),
    ]