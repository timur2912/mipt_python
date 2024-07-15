# Generated by Django 5.0.7 on 2024-07-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_alter_profile_phystech_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="checker",
            field=models.CharField(
                choices=[
                    ("", ""),
                    ("Павел Зверев", "Павел Зверев"),
                    ("Александр Маркин", "Александр Маркин"),
                    ("Готовский Геннадий", "Готовский Геннадий"),
                    ("Ромашкина Мария", "Ромашкина Мария"),
                ],
                default="",
                max_length=30,
                unique=True,
            ),
        ),
    ]
