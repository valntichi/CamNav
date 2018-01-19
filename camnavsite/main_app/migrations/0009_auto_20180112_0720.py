# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-12 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='blogs',
            new_name='article',
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]