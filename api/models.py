from django.db import models

class RequestData(models.Model):
    text = models.TextField(
        max_length=200,
        verbose_name="Текст",
        null=True,
        blank=True
    )
    url = models.TextField(
        verbose_name="Адрес url",
        null=True,
        blank=True
    )
    sender = models.CharField(
        max_length=55,
        verbose_name="Отправитель",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Данные запроса"
        verbose_name_plural = "Данные запросов"
