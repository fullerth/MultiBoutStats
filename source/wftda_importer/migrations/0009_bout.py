# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-15 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wftda_importer', '0008_auto_20160819_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
