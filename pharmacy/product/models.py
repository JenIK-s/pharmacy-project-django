from django.db import models

class Product(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок'
        )
    price = models.TextField(
        verbose_name='Цена'
    )

    class Meta:
        verbose_name='товар'
        verbose_name_plural='товары'

    def __str__(self):
        return self.title
