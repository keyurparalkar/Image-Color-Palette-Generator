from django.db import models
from django.core.validators import validate_image_file_extension
# Create your models here.
class ImageUploadModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='', validators=[validate_image_file_extension])

    # id = models.IntegerField(primary_key=True)
    # text_code = models.CharField(max_length=200)

    class Meta:
        ordering = ['-created']
    