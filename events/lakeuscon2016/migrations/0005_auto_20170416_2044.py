# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lakeuscon2016', '0004_signupextra_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupextra',
            name='shift_type',
            field=models.CharField(choices=[('yksipitka', 'Yksi pitkä vuoro'), ('montalyhytta', 'Monta lyhyempää vuoroa'), ('kaikkikay', 'Kumpi tahansa käy')], help_text='Haluatko tehdä yhden pitkän työvuoron vaiko monta lyhyempää vuoroa?', max_length=15, verbose_name='Toivottu työvuoron pituus'),
        ),
    ]
