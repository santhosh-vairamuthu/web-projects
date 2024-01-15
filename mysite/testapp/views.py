from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Items
from .forms import CreateNewList

def index(response, id):
    data = ToDoList.objects.get(id=id)
    return render(response, "testapp/base.html", {"name" : data.name})

def list(response):
    data = ToDoList.objects.get(id=1)
    return render(response, "testapp/list.html", {"data" : data})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "testapp/create.html", {"form" : form})

def home(response):
    return render(response, "testapp/home.html", {})
