from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    tg_chat_id = models.BigIntegerField(verbose_name='Чат ID', null=True)
    tg_username = models.CharField(max_length=255, default='', verbose_name='Telegram username')
    tg_first_name = models.CharField(max_length=255, default='', verbose_name='Telegram first_name')
    tg_last_name = models.CharField(max_length=255, default='', verbose_name='Telegram last_name')
    comments = models.CharField(max_length=255, default='', verbose_name='Комментарий')

    def __str__(self):
        return self.username
