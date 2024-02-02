"""
ASGI config for webunlock project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from facekeyapp.urls import websocket_urlpatterns
#from channels.auth import AuthMiddlewareStack

from django.urls import path
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webunlock.settings')
#django.setup()
#application = get_asgi_application()

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket":URLRouter(
#             websocket_urlpatterns
#         ),
#     }
# )
