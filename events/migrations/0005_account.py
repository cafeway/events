# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-11 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=30)),
                ('appointments', models.IntegerField()),
                ('time_arrival', models.DateField(default='12:00')),
            ],
        ),
    ]
