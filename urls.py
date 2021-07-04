from django.contrib import admin
from django.conf.urls import include, url
from django.urls import include
from django.urls import path
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login', views.login , name='login'),
    url(r'^structure$', views.get_structure , name='get_structure'),
    url(r'^check_structure$', views.check_structure , name='check_structure'),
    ]
