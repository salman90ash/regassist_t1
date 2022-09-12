from django.shortcuts import render
from rzn.models import Tasks, TasksKey
from users.models import CustomUser
from django.http import JsonResponse


# Create your views here.
def test():
    key = TasksKey()
    key.save()
    return JsonResponse({"success": True})

