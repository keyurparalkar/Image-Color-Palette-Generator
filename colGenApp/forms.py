from django import forms
from django.core.validators import FileExtensionValidator, validate_image_file_extension

class ImageUploadForm(forms.Form):
    img_file = forms.ImageField(required=True, validators=[validate_image_file_extension])