# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popeye', '0002_auto_20170919_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]