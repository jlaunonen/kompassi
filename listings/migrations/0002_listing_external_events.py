# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-16 13:07
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='external_events',
            field=models.ManyToManyField(to='listings.ExternalEvent'),
        ),
    ]
