from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import MyImage

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form=ImageForm()
        
    images = MyImage.objects.all()
    return render(request,'index.html',{'form': form, 'images':images})