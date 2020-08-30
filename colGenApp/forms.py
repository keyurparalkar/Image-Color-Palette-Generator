from django import forms
from django.core.validators import FileExtensionValidator

class ImageUploadForm(forms.Form):
    img_file = forms.ImageField(required=True, validators=[FileExtensionValidator(allowed_extensions=".jpg")])