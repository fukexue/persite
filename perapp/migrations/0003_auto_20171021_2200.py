# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perapp', '0002_personalabstract'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalabstract',
            old_name='abstract',
            new_name='Perabstract',
        ),
        migrations.RenameField(
            model_name='personalabstract',
            old_name='name',
            new_name='Pername',
        ),
    ]
