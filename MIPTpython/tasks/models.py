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
        verbose_name="Тип задания"
    )

    description_link = models.URLField(max_length=200,
                                       verbose_name="Ссылка на описание")
    deadline = models.DateTimeField(blank=True, null=True,
                                    verbose_name="Deadline")
    publish = models.BooleanField(default=False,
                                  verbose_name="Опубликовано")
    finished = models.BooleanField(default=False,
                                   verbose_name="Завершено")

    def __str__(self):
        return self.task_type



class Project1(models.Model):
    user_id = models.IntegerField(null=True)
    user_name = models.CharField(max_length=30, null=True, verbose_name="Фамилия и имя")
    link = models.URLField(max_length = 200, null=True, verbose_name="Ссылка")

    STATUS_CHOICES = (
        ("Сhecking", "Сhecking"),
        ("Rework", "Rework"),
        ("BLOCKED", "BLOCKED"),
        ("Accepted", "Accepted"),
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Сhecking",
        verbose_name="Статус",
    )
    checker = checker = models.CharField(
        max_length=30,
        # choices=CHECKER_CHOICES,
        default='',
        verbose_name="Проверяющий",
    )

    score = models.FloatField(null=True,
                              verbose_name="Баллы")

    class Meta:
        verbose_name = "Проект 1"
        verbose_name_plural = "Проект 1"


class Project2(models.Model):
    user_id = models.IntegerField(null=True)
    user_name = models.CharField(max_length=30, null=True, verbose_name="Фамилия и имя")
    link = models.URLField(max_length = 200, null=True, verbose_name="Ссылка")

    STATUS_CHOICES = (
        ("Сhecking", "Сhecking"),
        ("Rework", "Rework"),
        ("BLOCKED", "BLOCKED"),
        ("Accepted", "Accepted"),
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Сhecking",
        verbose_name="Статус",
    )
    checker = checker = models.CharField(
        max_length=30,
        # choices=CHECKER_CHOICES,
        default='',
        verbose_name="Проверяющий",
    )

    score = models.FloatField(null=True,
                              verbose_name="Баллы")

    class Meta:
        verbose_name = "Проект 2"
        verbose_name_plural = "Проект 2"


class Lab(models.Model):
    user_id = models.IntegerField(null=True)
    user_name = models.CharField(max_length=30, null=True, verbose_name="Фамилия и имя")
    link = models.URLField(max_length = 200, null=True, verbose_name="Ссылка")

    STATUS_CHOICES = (
        ("Сhecking", "Сhecking"),
        ("Rework", "Rework"),
        ("BLOCKED", "BLOCKED"),
        ("Accepted", "Accepted"),
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Сhecking",
        verbose_name="Статус",
    )
    checker = checker = models.CharField(
        max_length=30,
        # choices=CHECKER_CHOICES,
        default='',
        verbose_name="Проверяющий",
    )

    score = models.FloatField(null=True,
                              verbose_name="Баллы")

    class Meta:
        verbose_name = "Лабораторная работа"
        verbose_name_plural = "Лабораторная работа"
