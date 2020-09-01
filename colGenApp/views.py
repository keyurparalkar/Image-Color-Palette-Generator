from django.shortcuts import render
from .forms import ImageUploadForm
from .models import ImageUploadModel

from PIL import Image
from .image_utils import img_to_base64

# Create your views here.
def root_view(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            #save the image into the model:
            img_instance = ImageUploadModel(img=request.FILES['img_file'])
            img_instance.save()
            print("Image Saved to DATABASE....")


            img_obj = request.FILES['img_file']

            
            print(f'Value in form Data ==== {request.FILES["img_file"].__dict__}')            
            img_obj64_decoded = img_to_base64(img_obj.file)
            return render(request, 'colGenApp/index.html',{'form':form, 'img_obj':img_obj64_decoded})
    else:
        form = ImageUploadForm()
    
    return render(request, 'colGenApp/index.html',{'form':form})
