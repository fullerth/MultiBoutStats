# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-18 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wftda_importer', '0004_jam_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerToJam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
