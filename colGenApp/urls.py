from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter

from . import views
from .models import ImageUploadModel

router = DefaultRouter()
router.register(r'images',views.ImageViewSet)


urlpatterns = [
    path('', views.root_view, name="root_view"),
    path('data_list/',views.data_list, name='data_list'),
    path('all',include(router.urls))
]