# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-01 04:35
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20211201_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
    ]