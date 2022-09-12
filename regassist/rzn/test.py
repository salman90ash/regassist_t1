from rzn.models import Tasks, TasksKey, TasksData, TasksType, TasksNotice
from users.models import CustomUser
from django.http import JsonResponse
from django.db import transaction
import pickle
import json


@transaction.atomic
def test():
    key = TasksKey()
    key.save()
    notice = TasksNotice.objects.get(id=1)
    ttype = TasksType.objects.filter(title='РУ')[0]
    data = TasksData(rzn_number='12345',
                     rzn_date='08.08.2022',
                     url='test',
                     key=key,
                     notice=notice,
                     type=ttype
                     )
    data.save()
    user = CustomUser.objects.get(id=72)
    task = Tasks(title='New',
                 user=user,
                 data=data)
    task.save()
    return 'ok'

