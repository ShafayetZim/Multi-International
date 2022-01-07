from django.shortcuts import render
from .models import Service

# Create your views here.


def service(request):
    context = {
        'service': Service.objects.all(),
        'pageview': "Service"
    }
    return render(request, 'service.html', context)


def service_details(request):
    context = {
        # 'pageview': "Service"
        # 'service': Service.objects.all(),
    }
    return render(request, 'service-details.html', context)
