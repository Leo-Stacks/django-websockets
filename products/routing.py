from django.urls import path
from .consumers import ProductConsumer

websocket_urlpatterns = [
    path('ws/product_updates/', ProductConsumer.as_asgi()),
]
