"""
URL configuration for webunlock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#from facekeyapp.views import index, upload_video,stream_video


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('facekeyapp.urls')),
    #path('', include('facekeyapp.routing')),

    

    #path('bibhu/', views.bibhu)
    #path('bibhu/',views.main.as_view(),name='upload_image'),
    #path('upload_image/', views.upload_image),
    #path('', index, name='index'),
    #path('upload_video/', upload_video, name='upload_video'),
   


]


#from channels.middleware.websocket import WebSocketMiddleware

# from .consumers import YourConsumer

# websocket_urlpatterns = [
#     path('ws/some_path/', YourConsumer.as_asgi()),
# ]


# # routing.py
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack


# application = ProtocolTypeRouter(
#     {
#         "websocket": AuthMiddlewareStack(
#             URLRouter(
#                 [
#                     # Add your WebSocket consumers here
#                     # For example:
#                     path("ws/some_path/", YourConsumer.as_asgi()),
#                 ]
#             )
#         ),
#         # Add other protocol routes if needed
#     }
# )




