# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-02 02:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20190701_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
