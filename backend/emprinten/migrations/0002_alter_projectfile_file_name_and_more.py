# Generated by Django 5.0.2 on 2024-03-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("emprinten", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectfile",
            name="file_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name="projectfile",
            unique_together={("project", "file_name")},
        ),
    ]
