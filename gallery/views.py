from django.shortcuts import render
from .models import Gallery


def gallery(request):
    context = {
        'gallery': Gallery.objects.all(),
        'pageview': "Gallery",
    }
    return render(request, 'gallery.html', context)
