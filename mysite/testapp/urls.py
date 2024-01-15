from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name = "index"),
    path("home", views.home, name = "home"),
    path("list/<int:id>", views.list, name = "list"),
    path("create", views.create, name = "create"),
]