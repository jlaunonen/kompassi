# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-23 14:07
from django.db import migrations, models
import django.db.models.deletion
import labour.models.signup_extras


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0027_event_panel_css_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignupExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('shift_type', models.CharField(choices=[('none', 'Ei väliä'), ('4h', 'Pari pitkää vuoroa'), ('yli4h', 'Useita lyhyitä vuoroja')], help_text='Haluatko tehdä yhden pitkän työvuoron vaiko monta lyhyempää vuoroa?', max_length=15, verbose_name='Toivottu työvuoron pituus')),
                ('prior_experience', models.TextField(blank=True, help_text='Kerro tässä kentässä, jos sinulla on aiempaa kokemusta vastaavista tehtävistä tai muuta sellaista työkokemusta, josta arvioit olevan hyötyä hakemassasi tehtävässä.', verbose_name='Työkokemus')),
                ('free_text', models.TextField(blank=True, help_text='Jos haluat sanoa hakemuksesi käsittelijöille jotain sellaista, jolle ei ole omaa kenttää yllä, käytä tätä kenttää. Jos haet valokuvaajaksi, kerro lisäksi millaista kuvauskalustoa sinulla on käytettävissäsi ja listaamuutamia gallerialinkkejä, joista pääsemme ihailemaan ottamiasi kuvia. ', verbose_name='Vapaa alue')),
                ('special_diet_other', models.TextField(blank=True, help_text='Jos noudatat erikoisruokavaliota, jota ei ole yllä olevassa listassa, ilmoita se tässä. Tapahtuman järjestäjä pyrkii ottamaan erikoisruokavaliot huomioon, mutta kaikkia erikoisruokavalioita ei välttämättä pystytä järjestämään.', verbose_name='Muu erikoisruokavalio')),
                ('shirt_size', models.CharField(choices=[('NO_SHIRT', 'Ei paitaa'), ('XS', 'XS Unisex'), ('S', 'S Unisex'), ('M', 'M Unisex'), ('L', 'L Unisex'), ('XL', 'XL Unisex'), ('XXL', 'XXL Unisex'), ('3XL', '3XL Unisex'), ('4XL', '4XL Unisex'), ('5XL', '5XL Unisex'), ('LF_XS', 'XS Ladyfit'), ('LF_S', 'S Ladyfit'), ('LF_M', 'M Ladyfit'), ('LF_L', 'L Ladyfit'), ('LF_XL', 'XL Ladyfit')], default='NO_SHIRT', help_text='Ajoissa ilmoittautuneet saavat maksuttoman työvoimapaidan. Kokotaulukot: <a href="http://www.bc-collection.eu/uploads/sizes/TU004.jpg" target="_blank">unisex-paita</a>, <a href="http://www.bc-collection.eu/uploads/sizes/TW040.jpg" target="_blank">ladyfit-paita</a>', max_length=8, verbose_name='Paidan koko')),
                ('shirt_type', models.CharField(choices=[('STAFF', 'Staff'), ('DESURITY', 'Desurity'), ('KUVAAJA', 'Kuvaaja'), ('VENDOR', 'Myynti'), ('TOOLATE', 'Myöhästyi paitatilauksesta')], default='STAFF', max_length=8, verbose_name='Paidan tyyppi')),
                ('night_work', models.BooleanField(default=False, verbose_name='Olen valmis tekemään yötöitä')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frostbite2018_signup_extras', to='core.Event')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='frostbite2018_signup_extra', to='core.Person')),
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
        ),
        migrations.AddField(
            model_name='signupextra',
            name='special_diet',
            field=models.ManyToManyField(blank=True, related_name='_signupextra_special_diet_+', to='frostbite2018.SpecialDiet', verbose_name='Erikoisruokavalio'),
        ),
    ]
