# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-07 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('CLass', models.CharField(max_length=300)),
                ('adm', models.IntegerField()),
            ],
        ),
    ]
