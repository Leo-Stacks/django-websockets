"""
ASGI config for wsdjango project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wsdjango.settings')

django_asgi_app = get_asgi_application()
from django.urls import path
from chat.routing import websocket_urlpatterns
from products.consumers import ProductConsumer
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    "websocket": (
        (URLRouter([
            path('ws/product_updates/', ProductConsumer.as_asgi()),
        ]))
        # AuthMiddlewareStack(URLRouter([
        #     path('ws/product/', ProductConsumer.as_asgi()),
        # ]))
    ),
    # Just HTTP for now. (We can add other protocols later.)
})

