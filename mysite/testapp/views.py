from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Items

def index(response):
    return render(response, "testapp/base.html", {"name" : "god"})

def list(response):
    data = ToDoList.objects.get(id=1)
    return render(response, "testapp/list.html", {"data" : data})

def home(response):
    return render(response, "testapp/home.html", {})
