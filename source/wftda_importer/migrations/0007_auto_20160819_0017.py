# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-19 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wftda_importer', '0006_auto_20160818_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jam',
            name='players',
        ),
        migrations.AddField(
            model_name='jam',
            name='player',
            field=models.ManyToManyField(through='wftda_importer.PlayerToJam', to='wftda_importer.Player'),
        ),
        migrations.AddField(
            model_name='playertojam',
            name='position',
            field=models.CharField(choices=[('B', 'Blocker'), ('J', 'Jammer'), ('P', 'Pivot')], max_length=1, null=True),
        ),
    ]