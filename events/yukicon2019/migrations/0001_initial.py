# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-26 13:59
from django.db import migrations, models
import django.db.models.deletion
import labour.models.signup_extras


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0029_auto_20170827_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SignupExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('shift_type', models.CharField(choices=[('yksipitka', 'Yksi pitkä vuoro'), ('montalyhytta', 'Monta lyhyempää vuoroa'), ('kaikkikay', 'Kumpi tahansa käy')], help_text='Haluatko tehdä yhden pitkän työvuoron vaiko monta lyhyempää vuoroa?', max_length=15, verbose_name='Toivottu työvuoron pituus')),
                ('total_work', models.CharField(choices=[('10h', 'Minimi - 10 tuntia'), ('12h', '10-12 tuntia'), ('yli12h', 'Työn Sankari! Yli 12 tuntia!')], help_text='Kuinka paljon haluat tehdä töitä yhteensä tapahtuman aikana?', max_length=15, verbose_name='Toivottu kokonaistyömäärä')),
                ('want_certificate', models.BooleanField(default=False, verbose_name='Haluan todistuksen työskentelystäni Yukiconissa')),
                ('shirt_size', models.CharField(choices=[('NO_SHIRT', 'Ei paitaa'), ('XS', 'XS Unisex'), ('S', 'S Unisex'), ('M', 'M Unisex'), ('L', 'L Unisex'), ('XL', 'XL Unisex'), ('XXL', 'XXL Unisex'), ('3XL', '3XL Unisex'), ('4XL', '4XL Unisex'), ('5XL', '5XL Unisex')], default='NO_SHIRT', help_text='Ajoissa ilmoittautuneet vänkärit saavat maksuttoman työvoimapaidan.', max_length=8, verbose_name='Paidan koko')),
                ('special_diet_other', models.TextField(blank=True, help_text='Jos noudatat erikoisruokavaliota, jota ei ole yllä olevassa listassa, ilmoita se tässä. Tapahtuman järjestäjä pyrkii ottamaan erikoisruokavaliot huomioon, mutta kaikkia erikoisruokavalioita ei välttämättä pystytä järjestämään.', verbose_name='Muu erikoisruokavalio')),
                ('prior_experience', models.TextField(blank=True, help_text='Kerro tässä kentässä, jos sinulla on aiempaa kokemusta vastaavista tehtävistä tai muuta sellaista työkokemusta, josta arvioit olevan hyötyä hakemassasi tehtävässä.', verbose_name='Työkokemus')),
                ('shift_wishes', models.TextField(blank=True, help_text='Jos tiedät nyt jo, ettet pääse paikalle johonkin tiettyyn aikaan tai haluat osallistua johonkin tiettyyn ohjelmanumeroon, mainitse siitä tässä.', verbose_name='Alustavat työvuorotoiveet')),
                ('free_text', models.TextField(blank=True, help_text='Jos haluat sanoa hakemuksesi käsittelijöille jotain sellaista, jolle ei ole omaa kenttää yllä, käytä tätä kenttää.', verbose_name='Vapaa alue')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yukicon2019_signup_extras', to='core.Event')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='yukicon2019_signup_extra', to='core.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(labour.models.signup_extras.SignupExtraMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SpecialDiet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='signupextra',
            name='special_diet',
            field=models.ManyToManyField(blank=True, to='yukicon2019.SpecialDiet', verbose_name='Erikoisruokavalio'),
        ),
        migrations.AddField(
            model_name='signupextra',
            name='work_days',
            field=models.ManyToManyField(help_text='Minä päivinä olet halukas työskentelemään?', to='yukicon2019.EventDay', verbose_name='Tapahtumapäivät'),
        ),
    ]
