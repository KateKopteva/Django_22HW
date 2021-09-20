from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    lastname = models.CharField(max_length=255, verbose_name='Фамилия')
    year = models.DateField(verbose_name='Дата рождения')
    post = models.CharField(max_length=255, verbose_name='Должность')