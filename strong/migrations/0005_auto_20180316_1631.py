# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-16 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strong', '0004_auto_20180316_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='strong/'),
        ),
    ]