# Generated by Django 5.0.7 on 2024-07-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0013_project1_checker"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="finished",
            field=models.BooleanField(default=False),
        ),
    ]
