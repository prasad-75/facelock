from django.urls import path
from .views import main
from facekeyapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('webunlock.urls')),
    #path('bibhu/', views.bibhu)
    path('bibhu/',views.main.as_view(),name='upload_image'),
    #path('upload_image/', views.upload_image),
    #path('', index, name='index'),
    #path('upload_video/', upload_video, name='upload_video'),
   


]