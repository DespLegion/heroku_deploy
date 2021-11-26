from datetime import date

from django.db import models

# Create your models here.


class ApiList(models.Model):
    """Ссылка вызова Api с описанием"""
    requests_list = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE')
    )
    name = models.CharField('Название API', max_length=50)
    description = models.TextField('Подробное описание метода API', null=True)
    api_url = models.CharField('Ссылка для запроса API', max_length=100)
    add_date = models.DateField('Дата добавления метода', default=date.today)
    request_type = models.CharField(max_length=10, choices=requests_list)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Метод вызова API'
        verbose_name_plural = 'Методы вызова API'
