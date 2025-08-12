"""
ASGI config for PerfumeValley project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from whitenoise import WhiteNoise
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PerfumeValley.settings')
django.setup()

from . import routing

django_asgi_app = get_asgi_application()

# Wrap with WhiteNoise
static_root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../staticfiles')
django_asgi_app = WhiteNoise(django_asgi_app, root=static_root_path) 

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})

