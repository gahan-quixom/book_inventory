# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0008_auto_20170318_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrating',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_rating', to='details.Book'),
        ),
        migrations.AlterField(
            model_name='bookrating',
            name='rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]