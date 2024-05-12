from django.urls import path
from . import views

urlpatterns = [
    path("", views.products, name="products"),
    path("product/<str:pk>/", views.product, name="product"),
    path("update/<str:pk>/", views.updateProduct, name="update"),
    path("delete/<str:pk>/", views.deleteProduct, name="delete"),
    path("create/", views.createProduct, name="create"),
]