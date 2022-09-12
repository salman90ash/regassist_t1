from rzn.functions.settings import RZN_DOMAIN
from rzn.functions import actions
from rzn.models import Tasks, TasksKey, TasksData, TasksType, TasksNotice
from users.models import CustomUser
from django.db import transaction

# @transaction.atomic
# def test_add(number, date, type):
#     url = actions.set_url(number, date, type)
#     html = actions.get_page(url)
#     table = actions.get_table_of_cab_mi(html)
#     key_value = actions.get_key_of_cab_mi(table)
#
#
#     key = TasksKey()
#     key.value = key_value
#     key.save()
#     notice = TasksNotice.objects.get(id=1)
#     ttype = TasksType.objects.filter(title='РУ')[0]
#     data = TasksData(rzn_number='68225',
#                      rzn_date='23.09.2021',
#                      url='test',
#                      key=key,
#                      notice=notice,
#                      type=ttype
#                      )
#     data.save()
#     user = CustomUser.objects.get(id=72)
#     task = Tasks(title='New',
#                  user=user,
#                  data=data)
#     task.save()
#     return 'ok'
#


# Регистрация вх. 68225 ОТ 23.09.2021

number = '68225'
date = '23.09.2021'

@transaction.atomic
def add_task(number, date, type_code):
    url = actions.set_url(number, date, type_code)
    html = actions.get_page(url)
    table = actions.get_table_of_cab_mi(html)
    key_value = actions.get_key_of_cab_mi(table)
    key = TasksKey(value=key_value)
    key.save()
    notice = TasksNotice.objects.get(id=1)
    ttype = TasksType.objects.filter(title='РУ')[0]
    data = TasksData(rzn_number=number,
                     rzn_date=date,
                     url=url,
                     key=key,
                     notice=notice,
                     type=ttype
                     )
    data.save()
    user = CustomUser.objects.get(id=1)
    task = Tasks(title='FGM',
                 user=user,
                 data=data)
    task.save()
    return 'ok'

@transaction.atomic
def add_task(user_id, type_id, number, date):
    url = actions.set_url(number, date, type_id)
    html = actions.get_page(url)
    table = actions.get_table_of_cab_mi(html)
    key_value = actions.get_key_of_cab_mi(table)
    key = TasksKey(value=key_value)
    key.save()
    notice = TasksNotice.objects.get(id=1)
    type = TasksType.objects.get(id=type_id)
    data = TasksData(rzn_number=number,
                     rzn_date=date,
                     url=url,
                     key=key,
                     notice=notice,
                     type=type
                     )
    data.save()
    user = CustomUser.objects.get(id=user_id)
    task = Tasks(title='FGM',
                 user=user,
                 data=data)
    task.save()
    return 'ok'

add_task(number, date, 1)
