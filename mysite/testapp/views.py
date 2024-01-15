from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .models import ToDoList, Items
from .forms import CreateNewList

def index(response, id):
    data = ToDoList.objects.get(id=id)
    

    return render(response, "testapp/base.html", {"name" : data.name})

def list(response, id):
    data = ToDoList.objects.get(id=id)
    if response.method == "POST":
        if response.POST.get("save") == "save":
            for i in data.items_set.all():
                if response.POST.get("c"+str(i.id)) == "clicked":
                    i.complete = True 
                else:
                    i.complete = False
                i.save()
        elif response.POST.get("add_new") == "add_new":
            if len(response.POST.get("new")) >= 2:
                data.items_set.create(text=response.POST.get("new"))
            return redirect("/list/" + str(id))
    return render(response, "testapp/list.html", {"data": data})


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
