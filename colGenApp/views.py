from django.shortcuts import render
from .forms import ImageUploadForm

# Create your views here.
def root_view(request):
    print(f"REQUEST METHOD TYPE ========= {request.method}")
    form = ImageUploadForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            print("IMAGE NAME === ", form.cleaned_data.get('name'))
            print("POST SUCCESS")
            return render(request, 'colGenApp/index.html',{'form':form})
    else:
        form = ImageUploadForm()
    
    return render(request, 'colGenApp/index.html',{'form':form})
