# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-10-22 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faconstor', '0045_step_force_exec'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientGUID', models.CharField(max_length=50, null=True, verbose_name='GUID')),
                ('clientName', models.CharField(max_length=200, verbose_name='主机名称')),
                ('owernID', models.CharField(blank=True, max_length=50, null=True, verbose_name='用户GUID')),
                ('hostType', models.CharField(blank=True, max_length=50, null=True, verbose_name='主机类型')),
                ('vendor', models.CharField(blank=True, max_length=1000, null=True, verbose_name='vendor')),
                ('zone', models.CharField(blank=True, max_length=1000, null=True, verbose_name='zone')),
                ('clientID', models.IntegerField(blank=True, null=True, verbose_name='主机ID')),
                ('proxyClientID', models.CharField(blank=True, max_length=5000, null=True, verbose_name='代理主机列表')),
                ('creditInfo', models.CharField(blank=True, max_length=1000, null=True, verbose_name='认证信息')),
                ('agentTypeList', models.CharField(blank=True, max_length=2000, null=True, verbose_name='代理类型列表')),
                ('status', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态')),
                ('platform', models.CharField(blank=True, max_length=50, null=True, verbose_name='平台')),
                ('appGroup', models.CharField(blank=True, max_length=50, null=True, verbose_name='应用组')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True, verbose_name='描述')),
                ('installTime', models.DateTimeField(blank=True, null=True, verbose_name='安装时间')),
                ('activeTime', models.DateTimeField(blank=True, null=True, verbose_name='激活时间')),
                ('firstProtectTime', models.DateTimeField(blank=True, null=True, verbose_name='首次保护时间')),
                ('lastProtectTime', models.DateTimeField(blank=True, null=True, verbose_name='最近保护时间')),
            ],
        ),
    ]
