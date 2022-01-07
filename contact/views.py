from django.shortcuts import render
from .models import Contact


def contact(request):
    context = {
        'contact': Contact.objects.all(),
        'pageview': "Contact",
    }
    return render(request, 'contact.html', context)
