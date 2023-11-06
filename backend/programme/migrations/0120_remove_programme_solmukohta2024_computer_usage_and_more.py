# Generated by Django 4.2.7 on 2023-11-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("solmukohta2024", "0002_technology"),
        ("programme", "0119_programme_hosts_from_host_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="programme",
            name="solmukohta2024_computer_usage",
        ),
        migrations.AddField(
            model_name="programme",
            name="aweek2024_participants",
            field=models.CharField(
                blank=True, default="", max_length=1023, verbose_name="For how many people your program item is for?"
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="aweek2024_prepare",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Do the participants need to prepare somehow?",
                max_length=1023,
                verbose_name="Preparations required",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="aweek2024_signup",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Does your program item need sign-up or is it free for everyone to attend?",
                max_length=1023,
                verbose_name="Sign-up requirements",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="aweek2024_when",
            field=models.TextField(
                blank=True,
                default="",
                help_text="A Week-in is happening from Monday to Wednesday. Check above the available times at the main location Artteli. Please include your preparation time on the location as well, if your programme item is happening at Artteli. We do our best to make things not overlap!",
                verbose_name="When would you like to run your programme?",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="solmukohta2024_technology",
            field=models.ManyToManyField(blank=True, to="solmukohta2024.technology", verbose_name="Technical needs"),
        ),
        migrations.AlterField(
            model_name="programme",
            name="solmukohta2024_have_you_hosted_before",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", ""),
                    ("many", "Yes, many times"),
                    ("couple", "Yes, a couple of times"),
                    ("few", "Yes, once or twice"),
                    ("nope", "No, this is my first time"),
                ],
                default="",
                max_length=6,
                verbose_name="Have you hosted program for SK/KP before?",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="solmukohta2024_ticket",
            field=models.BooleanField(
                default=False,
                help_text="I understand that if my programme item is accepted, I will still need to purchase a Solmukohta 2024 ticket in order to attend.",
                verbose_name="I have purchased or am about to purchase a Solmukohta 2024 ticket",
            ),
        ),
    ]