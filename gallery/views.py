from django.shortcuts import render
from .models import Image


# Create your views here.

def home(request):
    context = {
        'images':Image.get_all_images()
    }
    return render(request,'gallery/home.html', context)

