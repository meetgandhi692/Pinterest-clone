# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 22:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pinterest.Pin'),
        ),
    ]
