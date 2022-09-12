import datetime

from django.db import models
from regassist.settings import AUTH_USER_MODEL


# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    data = models.ForeignKey('TasksData', on_delete=models.CASCADE, verbose_name='Сведения')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


class TasksType(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    is_active = models.BooleanField(default=True, blank=True, verbose_name='Активировать')

    def __str__(self):
        return self.title


class TasksNotice(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    is_active = models.BooleanField(default=True, blank=True, verbose_name='Активировать')

    def __str__(self):
        return self.title


class TasksKey(models.Model):
    value = models.JSONField(default={}, blank=True, verbose_name='Ключ')
    date_create = models.DateTimeField(auto_now_add=True)


class TasksData(models.Model):
    rzn_number = models.CharField(max_length=255, verbose_name='Вх. номер', null=True)
    rzn_date = models.CharField(max_length=255, verbose_name='Вх. дата', null=True)
    dec_number = models.CharField(max_length=255, verbose_name='Исх. номер', null=True)
    dec_date = models.CharField(max_length=255, verbose_name='Исх. дата', null=True)
    url = models.CharField(max_length=255, verbose_name='URL', null=True)
    completed = models.BooleanField(default=False, blank=True, verbose_name='Завершено', null=True)
    date_UPD = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', null=True)
    key = models.ForeignKey('TasksKey', on_delete=models.CASCADE, null=True)
    notice = models.ForeignKey('TasksNotice', on_delete=models.CASCADE, null=True)
    type = models.ForeignKey('TasksType', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
