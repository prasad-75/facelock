from django.urls import path
from facekeyapp import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('webunlock.urls')),
    path('',views.main.as_view()),
    #path('bibhu/',views.main.post),
    #path('upload_image/', views.upload_image),
    #path('', index, name='index'),
    #path('upload_video/', upload_video, name='upload_video')
   


]

# from django.urls import re_path

# from . import consumers 
# websocket_urlpatterns = [
#     re_path(r'ws/facekeyapp/$',consumers.VideoStreamConsumer.as_asgi()),
# ] 