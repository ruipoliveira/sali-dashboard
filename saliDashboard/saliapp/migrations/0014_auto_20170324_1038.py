# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saliapp', '0013_auto_20170324_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='smpercm',
            name='id',
            field=models.AutoField(auto_created=True, default=8, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smpercm',
            name='id_cm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saliapp.ControllerModule'),
        ),
    ]
