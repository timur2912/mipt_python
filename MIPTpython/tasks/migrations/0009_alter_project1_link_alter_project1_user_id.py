# Generated by Django 5.0.7 on 2024-07-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0008_alter_project1_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project1",
            name="link",
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name="project1",
            name="user_id",
            field=models.IntegerField(null=True),
        ),
    ]
