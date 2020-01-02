# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-09-08 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faconstor', '0025_auto_20190904_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('status', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态')),
            ],
        ),
    ]