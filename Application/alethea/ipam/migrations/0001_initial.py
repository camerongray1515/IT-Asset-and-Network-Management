# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DhcpRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_address', models.CharField(max_length=255)),
                ('end_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('descripton', models.TextField()),
                ('is_failover', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Subnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('netmask', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='subnet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipam.Subnet'),
        ),
        migrations.AddField(
            model_name='dhcprange',
            name='subnet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipam.Subnet'),
        ),
    ]