# Generated by Django 4.1 on 2022-08-20 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rzn', '0009_tasksnotice_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasksnotice',
            old_name='active',
            new_name='is_active',
        ),
    ]
