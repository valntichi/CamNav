# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-11 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
