from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from . import views
from .serializers import ImageSerializer
from .models import ImageUploadModel

#creating viewsets to define view behaviour
class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageUploadModel.objects.all()
    serializer_class = ImageSerializer

router = routers.DefaultRouter()
router.register(r'all_imgs', ImageViewSet)


urlpatterns = [
    path('', views.root_view, name="root_view")
]