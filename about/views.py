from django.shortcuts import render
from .models import About, Vision, Team, Choice

# Create your views here.

def about(request):
    context = {
        'about': About.objects.all(),
        'vision': Vision.objects.all(),
        'team': Team.objects.all(),
        'choice': Choice.objects.all(),
        'pageview': "About",
    }
    return render(request, 'about.html', context)
