# Generated by Django 5.0.7 on 2024-07-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0012_profile_fathers_name"),
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
            ),
        ),
    ]
