# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-06 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lakeuscon2016', '0002_auto_20160221_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupextra',
            name='signup',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='lakeuscon2016_signup_extra', serialize=False, to='labour.Signup'),
        ),
    ]
