from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=18, blank=True, null=True)
    first_name = models.CharField(max_length=18, blank=True, null=True)
    fathers_name = models.CharField(max_length=18, blank=True, null=True)
    GROUP_CHOICES = (('', ''),
                     ('Б05-301', 'Б05-301'),
                     ('Б05-302', 'Б05-302'),
                     ('Б05-303', 'Б05-303'),
                     ('Б05-304', 'Б05-304'),
                     ('Б05-305', 'Б05-305'),
                     )

    group = models.CharField(
        max_length=7,
        choices= GROUP_CHOICES,
        default='',
    )

    flow = models.CharField(
        max_length=30,
        choices= (('', ''), ("Базовый", "Базовый"), ("Продвинутый", "Продвинутый")),
        default='',
    )

    SEMINARISTS_CHOICES = (
        ('', ''),
        ("Павел Зверев", "Павел Зверев"),
        ("Александр Маркин", "Александр Маркин"),
        ("Готовский Геннадий", "Готовский Геннадий"),
        ("Ромашкина Мария", "Ромашкина Мария"),
    )

    seminarist = models.CharField(
        max_length=30,
        choices=SEMINARISTS_CHOICES,
        default='',
    )

    CHECKER_CHOICES = [
        ('', ''),
        ('Павел Зверев', 'Павел Зверев'),
        ("АлександрМаркин", "Александр Маркин"),
        ("Геннадий Готовский", "Геннадий Готовский"),
        ("Ромашкина Мария", "Ромашкина Мария"),
    ]

    checker = models.TextField(
        max_length=40,
        choices=CHECKER_CHOICES,
        default='',
    )

    phystech_email = models.EmailField(max_length=254, blank=True, null=True)
    telegram = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

