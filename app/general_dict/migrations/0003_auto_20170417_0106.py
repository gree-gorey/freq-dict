# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_dict', '0002_byyear'),
    ]

    operations = [
        migrations.RenameField(
            model_name='byyear',
            old_name='freq_fiction',
            new_name='fiction_50_60',
        ),
        migrations.RenameField(
            model_name='byyear',
            old_name='freq_news',
            new_name='fiction_70_80',
        ),
        migrations.RenameField(
            model_name='byyear',
            old_name='freq_nonfiction',
            new_name='fiction_90_00',
        ),
        migrations.RenameField(
            model_name='byyear',
            old_name='freq_spoken',
            new_name='news_50_60',
        ),
        migrations.AddField(
            model_name='byyear',
            name='news_70_80',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='byyear',
            name='news_90_00',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]