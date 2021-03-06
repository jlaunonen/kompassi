# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('core', '0003_auto_20150813_1907'),
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSEventMeta',
            fields=[
                ('event', models.OneToOneField(related_name='smseventmeta', primary_key=True, serialize=False, to='core.Event')),
                ('sms_enabled', models.BooleanField(default=False)),
                ('current', models.BooleanField(default=False)),
                ('used_credit', models.IntegerField(default=0)),
                ('admin_group', models.ForeignKey(to='auth.Group')),
            ],
            options={
                'verbose_name': 'Tekstiviestej\xe4 k\xe4ytt\xe4v\xe4 tapahtuma',
                'verbose_name_plural': 'Tekstiviestej\xe4 k\xe4ytt\xe4v\xe4t tapahtumat',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='smsevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='smsmessagein',
            name='smsevent',
        ),
        migrations.AddField(
            model_name='smsmessagein',
            name='SMSEventMeta',
            field=models.ForeignKey(default=1, to='sms.SMSEventMeta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smsmessageout',
            name='event',
            field=models.ForeignKey(to='sms.SMSEventMeta'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='SMSEvent',
        ),
    ]
