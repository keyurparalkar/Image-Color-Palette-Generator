from rest_framework import serializers
from .models import ImageUploadModel

# class ImageSerializer(serializers.Serializer):
#     img = serializers.ImageField(upload_to='')

#     def create(self, validated_data):
#         print(validated_data)
#         print(f"Validated_data TYPE == {type(validated_data)}")
#         return ImageUploadModel.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.img = validated_data.get('img', instance.img)
#         instance.save()
#         return instance


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUploadModel
        fields = ['created','img']

        