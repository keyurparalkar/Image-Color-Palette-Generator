from django.shortcuts import render
from .forms import ImageUploadForm
import base64

# Create your views here.
def root_view(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img_obj = request.FILES['img_file'].read()
            img_obj64_bytes = base64.b64encode(img_obj)
            img_obj64_decoded = img_obj64_bytes.decode('ascii')
            return render(request, 'colGenApp/index.html',{'form':form, 'img_obj':img_obj64_decoded})
    else:
        form = ImageUploadForm()
    
    return render(request, 'colGenApp/index.html',{'form':form})
