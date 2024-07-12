from django.db import models

class Task(models.Model):
    TASKS_CHOICES = (
        ("0", "0"),
        ("1", "Контест"),
        ("2", "Проект 1"),
        ("3", "Проект 2"),
        ("4", "Лабораторная работа по анлизу данных"),
    )

    task_type = models.CharField(
        max_length=30,
        choices=TASKS_CHOICES,
        default='0',
        unique=True,
    )
    description_link = models.URLField(max_length=200)
    deadline = models.DateTimeField(blank=True, null=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.task_type

class Project1(models.Model):
    user_id = models.IntegerField(null=True)
    user_name = models.CharField(max_length=30, null=True)
    link = models.URLField(max_length = 200, null=True)

    STATUS_CHOICES = (
        ("Сhecking", "Сhecking"),
        ("Rework", "Rework"),
        ("Accepted", "Accepted"),
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Сhecking",
    )
    score = models.FloatField(null=True)
