# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-27 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_auto_20170227_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='back.Author'),
        ),
    ]
