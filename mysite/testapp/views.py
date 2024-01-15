from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Items

def index(response):
    data = ToDoList.objects.get(id=1)
    return HttpResponse("<h1>%s</h1>" % data.name)
