# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-19 20:22
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0066_programme_ropecon2018_preferred_time_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='length_from_host',
            field=models.CharField(blank=True, help_text='Huomaathan, että emme voi taata juuri toivomasi pituista ohjelmapaikkaa. Ohjelmavastaava vahvistaa ohjelmasi pituuden.', max_length=127, null=True, verbose_name='Ohjelman pituus'),
        ),
        migrations.AddField(
            model_name='programme',
            name='long_description',
            field=models.TextField(blank=True, default='', help_text='Kuvaile ohjelmaasi tarkemmin ohjelmavastaavalle. Minkälaista rakennetta olet ohjelmallesi suunnitellut? Millaisia asioita tulisit käsittelemään? Kerro myös onko ohjelmasi suunnattu aloittevammille vai kokeneemmille harrastajille.', verbose_name='Tarkempi kuvaus'),
        ),
    ]
