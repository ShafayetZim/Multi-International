from django.shortcuts import render
from .models import Base, Feature, WorkingProcess, Slider


# from django.views.generic import ListView

# Create your views here.
# class Template(ListView):
#     model = Base
#     template_name = 'base.html'
#     context_object_name = 'base'

def index(request):
    # base = Base.objects.last()
    # print(base.header_phone)
    context = {
        'base': Base.objects.all(),
        'feature': Feature.objects.all(),
        'process': WorkingProcess.objects.all(),
        'slider': Slider.objects.all(),
        'pageview': "Home"
    }
    return render(request, 'index.html', context)


def layout(request):
    base = Base.objects.all()

    for item in base:
        print(item.header_logo)
        print(item.header_phone)
    return render(request, 'base.html', {'base': base})


def example(request):
    context = {
        'about1': Base.objects.all(),
        'about2': Base2.objects.all(),
        'about3': Base3.objects.all(),
    }
    return render(request, 'example.html', context)

