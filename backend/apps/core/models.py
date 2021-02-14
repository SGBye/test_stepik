from django.db import models


class Solution(models.Model):
    STATUS_CHOICES = [
        ("evaluation", "Оценивается"),
        ("correct", "Верно"),
        ("wrong", "Неверно"),
        ("unevaluated", "Серверная ошибка при оценивании"),
    ]

    start_dt = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=32, default="evaluation")
    code = models.TextField()
    checker_identifier = models.BigIntegerField(null=True, blank=True)

