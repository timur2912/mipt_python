# Generated by Django 5.0.7 on 2024-07-15 21:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0016_alter_profile_checker"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="checker",
            field=models.TextField(
                choices=[
                    ("", ""),
                    ("ПавелЗверев", "ПавелЗверев"),
                    ("АлександрМаркин", "Александр Маркин"),
                    ("Геннадий Готовский", "Геннадий Готовский"),
                    ("Ромашкина Мария", "Ромашкина Мария"),
                ],
                default="",
                max_length=40,
            ),
        ),
    ]
