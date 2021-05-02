from django.contrib import admin
from django.urls import path
from app import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('student', views.student),
    path('start', csrf_exempt(views.startdn)),
    path('stop', csrf_exempt(views.stopdn))
]
