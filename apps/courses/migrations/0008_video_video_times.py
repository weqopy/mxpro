# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-24 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_times',
            field=models.IntegerField(default=0, verbose_name='视频长度（分钟数）'),
        ),
    ]