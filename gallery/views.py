from django.shortcuts import render
from .models import Image


# Create your views here.

def home(request):
    context = {
        'images':Image.get_all_images()
    }
    return render(request,'gallery/home.html', context)

def filter_by_search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        images = Image.filter_images_by_search(search_term)
        message = f"{search_term}"
        context = {
            "message":message,
            "images":images
        }

        return render(request, 'gallery/search.html', context)
    else:
        
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html')