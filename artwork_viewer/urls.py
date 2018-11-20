from django.contrib import admin
from django.urls import path, include
from artview import views

urlpatterns = [


    path('admin/', admin.site.urls),
    path('', views.mainpage , name='mainpage'),
    path('artview/', include('artview.urls',namespace='artview')),

]
