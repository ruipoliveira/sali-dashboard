# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saliapp', '0012_auto_20170322_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smpercm',
            name='id',
        ),
        migrations.AlterField(
            model_name='smpercm',
            name='id_cm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='saliapp.ControllerModule'),
        ),
    ]