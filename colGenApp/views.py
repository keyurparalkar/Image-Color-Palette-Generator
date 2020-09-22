from django.shortcuts import render
from django.http import JsonResponse

from .forms import ImageUploadForm
from .models import ImageUploadModel
from .serializers import ImageSerializer

from PIL import Image
from .image_utils import img_to_base64, hex_colors

# Create your views here.
def root_view(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print(f'Request File Type = {type(request.FILES["img_file"])}')
            #save the image into the model:
            img_instance = ImageUploadModel(img=request.FILES['img_file'])
            img_instance.save()
            print("Image Saved to DATABASE....")


            img_obj = request.FILES['img_file']

            
            # print(f'Value in form Data ==== {img_obj.__dict__}')            
            img_obj64_decoded = img_to_base64(img_obj.file)
            
            hex_values = hex_colors(img_obj, 4)
            print(f'HEX VALUES = {hex_values}')
            return render(request, 'colGenApp/index.html',{'form':form, 'img_obj':img_obj64_decoded, 'hex_vals':hex_values})
    else:
        form = ImageUploadForm()
    
    return render(request, 'colGenApp/index.html',{'form':form})


def data_list(request):
    if request.method == 'GET':
        objs = ImageUploadModel.objects.all()
        sz = ImageSerializer(objs, many=True)
        return JsonResponse(sz.data, safe=False)