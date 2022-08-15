from django.db import models


# Create your models here.

# class Tasks(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Наименование')
#     user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True)


class TasksType(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')


class TasksNotice(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')


class TasksKey(models.Model):
    value = models.JSONField(verbose_name='Ключ')
    date_create = models.DateTimeField(auto_now_add=True)


class TasksData(models.Model):
    type_id = models.ForeignKey('TasksType', on_delete=models.CASCADE, null=True)
    rzn_number = models.CharField(max_length=255, verbose_name='Вх. номер')
    rzn_date = models.CharField(max_length=255, verbose_name='Вх. дата')
    dec_number = models.CharField(max_length=255, verbose_name='Исх. номер')
    dec_date = models.CharField(max_length=255, verbose_name='Исх. дата')
    key_id = models.ForeignKey('TasksKey', on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length=255, verbose_name='URL')
    notice_id = models.ForeignKey('TasksNotice', on_delete=models.CASCADE, null=True)
    completed = models.BooleanField(default=False, verbose_name='Завершено')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_UPD = models.DateTimeField(auto_now=True, verbose_name='Дата создания')