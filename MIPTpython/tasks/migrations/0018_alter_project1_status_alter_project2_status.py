# Generated by Django 5.0.7 on 2024-07-21 21:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0017_alter_lab_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project1",
            name="status",
            field=models.CharField(
                choices=[
                    ("Сhecking", "Сhecking"),
                    ("Rework", "Rework"),
                    ("BLOCKED", "BLOCKED"),
                    ("Accepted", "Accepted"),
                ],
                default="Сhecking",
                max_length=30,
                verbose_name="Статус",
            ),
        ),
        migrations.AlterField(
            model_name="project2",
            name="status",
            field=models.CharField(
                choices=[
                    ("Сhecking", "Сhecking"),
                    ("Rework", "Rework"),
                    ("BLOCKED", "BLOCKED"),
                    ("Accepted", "Accepted"),
                ],
                default="Сhecking",
                max_length=30,
                verbose_name="Статус",
            ),
        ),
    ]
