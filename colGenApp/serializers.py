from .models import ImageUploadModel
from rest_framework import serializers

class ImageSerializer(serializers.Serializer):
    img =  serializers.ImageField(required=True)

    def create(self, validated_data):
        return ImageUploadModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance