# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 11:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='base',
            name='camp2',
        ),
    ]
