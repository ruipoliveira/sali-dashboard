# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 22:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saliapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communicationtype',
            old_name='path_or_nu',
            new_name='path_or_number',
        ),
    ]
