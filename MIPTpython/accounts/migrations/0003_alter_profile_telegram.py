# Generated by Django 5.0.7 on 2024-07-15 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_remove_profile_bio_profile_checker_profile_flow_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="telegram",
            field=models.URLField(blank=True, null=True),
        ),
    ]
