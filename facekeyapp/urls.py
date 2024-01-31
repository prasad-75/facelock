from django.urls import path
from facekeyapp import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('webunlock.urls')),
    path('',views.main.as_view()),
    #path('bibhu/',views.main.post),
    #path('upload_video/', upload_video, name='upload_video')
   


]