from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):
    img = models.ImageField(upload_to='')