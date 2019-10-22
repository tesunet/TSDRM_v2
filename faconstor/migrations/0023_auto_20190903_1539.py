# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-09-03 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faconstor', '0022_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='origin',
            name='target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='faconstor.Target', verbose_name='默认关联终端'),
        ),
    ]
