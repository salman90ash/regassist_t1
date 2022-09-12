# Generated by Django 4.1 on 2022-08-24 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rzn', '0013_alter_tasksdata_completed_alter_tasksdata_date_upd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rzn.tasksdata', verbose_name='Сведения'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]