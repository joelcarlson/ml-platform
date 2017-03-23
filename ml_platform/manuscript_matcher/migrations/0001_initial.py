# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_name', models.CharField(max_length=100)),
                ('jcr_category', models.CharField(max_length=100)),
                ('jcr_rank', models.CharField(max_length=100)),
                ('jcr_quartile', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('issn', models.CharField(max_length=100)),
                ('eissn', models.CharField(max_length=100)),
                ('jif', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('journal_name',),
            },
        ),
    ]