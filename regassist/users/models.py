from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    fio = models.CharField('ФИО', max_length=255, default='')

    def __str__(self):
        return self.username
