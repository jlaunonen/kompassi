# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labour', '0006_auto_20141115_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcategory',
            name='personnel_classes',
            field=models.ManyToManyField(to='labour.PersonnelClass', verbose_name='yhteiskuntaluokat', blank=True),
            preserve_default=True,
        ),
    ]
