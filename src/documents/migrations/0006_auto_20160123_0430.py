# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-23 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_auto_20160123_0313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(blank=True)),
                ('colour', models.PositiveIntegerField(choices=[(1, '#a6cee3'), (2, '#1f78b4'), (3, '#b2df8a'), (4, '#33a02c'), (5, '#fb9a99'), (6, '#e31a1c'), (7, '#fdbf6f'), (8, '#ff7f00'), (9, '#cab2d6'), (10, '#6a3d9a'), (11, '#ffff99'), (12, '#b15928'), (13, '#000000'), (14, '#cccccc')], default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='sender',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.ManyToManyField(related_name='documents', to='documents.Tag'),
        ),
    ]
