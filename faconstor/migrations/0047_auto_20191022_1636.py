# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-10-22 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faconstor', '0046_clienthost'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackupResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='名称')),
                ('certificate', models.CharField(blank=True, max_length=5000, null=True, verbose_name='证书')),
                ('specifications', models.CharField(blank=True, max_length=5000, null=True, verbose_name='规格')),
                ('cost', models.IntegerField(blank=True, null=True, verbose_name='成本')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='描述')),
                ('state', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态')),
                ('creatdate', models.DateTimeField(blank=True, null=True, verbose_name='创建时间')),
                ('updatedate', models.DateTimeField(blank=True, null=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataSetGUID', models.CharField(max_length=50, null=True, verbose_name='GUID')),
                ('clientGUID', models.CharField(max_length=50, null=True, verbose_name='主机GUID')),
                ('clientName', models.CharField(max_length=200, verbose_name='主机名称')),
                ('owernID', models.CharField(blank=True, max_length=50, null=True, verbose_name='用户GUID')),
                ('vendor', models.CharField(blank=True, max_length=1000, null=True, verbose_name='vendor')),
                ('zone', models.CharField(blank=True, max_length=1000, null=True, verbose_name='zone')),
                ('clientID', models.IntegerField(blank=True, null=True, verbose_name='主机ID')),
                ('instanceName', models.CharField(blank=True, max_length=500, null=True, verbose_name='实例名称')),
                ('agentType', models.CharField(blank=True, max_length=50, null=True, verbose_name='代理类型')),
                ('credit', models.CharField(blank=True, max_length=1000, null=True, verbose_name='认证信息')),
                ('status', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态')),
                ('appGroup', models.CharField(blank=True, max_length=50, null=True, verbose_name='应用组名称')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True, verbose_name='描述')),
                ('content', models.CharField(blank=True, max_length=5000, null=True, verbose_name='保护内容')),
                ('installTime', models.DateTimeField(blank=True, null=True, verbose_name='安装时间')),
                ('activeTime', models.DateTimeField(blank=True, null=True, verbose_name='激活时间')),
                ('firstProtectTime', models.DateTimeField(blank=True, null=True, verbose_name='首次保护时间')),
                ('lastProtectTime', models.DateTimeField(blank=True, null=True, verbose_name='最近保护时间')),
            ],
        ),
        migrations.CreateModel(
            name='ResourcePool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='名称')),
                ('type', models.CharField(blank=True, max_length=20, null=True, verbose_name='类型')),
                ('supplier', models.CharField(blank=True, max_length=50, null=True, verbose_name='供应商')),
                ('certificate', models.CharField(blank=True, max_length=5000, null=True, verbose_name='证书')),
                ('specifications', models.CharField(blank=True, max_length=5000, null=True, verbose_name='规格')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='描述')),
                ('level', models.CharField(blank=True, max_length=10, null=True, verbose_name='级别')),
                ('state', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态')),
                ('creatdate', models.DateTimeField(blank=True, null=True, verbose_name='创建时间')),
                ('updatedate', models.DateTimeField(blank=True, null=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='SchduleResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='名称')),
                ('certificate', models.CharField(blank=True, max_length=5000, null=True, verbose_name='证书')),
                ('specifications', models.CharField(blank=True, max_length=5000, null=True, verbose_name='规格')),
                ('cost', models.IntegerField(blank=True, null=True, verbose_name='成本')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='描述')),
                ('state', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态')),
                ('creatdate', models.DateTimeField(blank=True, null=True, verbose_name='创建时间')),
                ('updatedate', models.DateTimeField(blank=True, null=True, verbose_name='修改时间')),
                ('pool', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='faconstor.ResourcePool')),
            ],
        ),
        migrations.AddField(
            model_name='backupresource',
            name='pool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='faconstor.ResourcePool'),
        ),
    ]