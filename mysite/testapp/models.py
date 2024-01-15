from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Items(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300, default=None)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
