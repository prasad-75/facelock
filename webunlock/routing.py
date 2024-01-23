
from django.urls import re_path
from facekeyapp import consumers


websocket_urlpatterns = [
    re_path(r'ws/facekeyapp/$', consumers.VideoStreamConsumer.as_asgi()),
] 