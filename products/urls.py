from django.urls import path

from . import views


urlpatterns = [
    path("add/", views.add_product, name="Add Product"),
    path("list/", views.products, name="Products"),
    path("<str:pk>/", views.product, name="Product"),
]
