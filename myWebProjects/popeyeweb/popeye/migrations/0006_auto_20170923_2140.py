# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popeye', '0005_contentwriting_websitebuilding'),
    ]

    operations = [
        migrations.RenameField(
            model_name='websitebuilding',
            old_name='additional_intructions',
            new_name='additional_instructions',
        ),
    ]