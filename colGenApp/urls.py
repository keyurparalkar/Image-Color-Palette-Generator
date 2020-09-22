from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from . import views
from .models import ImageUploadModel


urlpatterns = [
    path('', views.root_view, name="root_view"),
    path('data_list/',views.data_list, name='data_list')
]