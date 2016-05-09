# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-08 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('nowDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
