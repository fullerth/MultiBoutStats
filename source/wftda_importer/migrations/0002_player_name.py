# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wftda_importer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
