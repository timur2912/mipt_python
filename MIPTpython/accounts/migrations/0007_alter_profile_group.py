# Generated by Django 5.0.7 on 2024-07-15 12:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_alter_profile_flow_alter_profile_seminarists"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="group",
            field=models.CharField(
                choices=[
                    ("", ""),
                    ("Б05-301", "Б05-301"),
                    ("Б05-302", "Б05-302"),
                    ("Б05-303", "Б05-303"),
                    ("Б05-304", "Б05-304"),
                    ("Б05-305", "Б05-305"),
                ],
                default="",
                max_length=7,
                unique=True,
            ),
        ),
    ]
