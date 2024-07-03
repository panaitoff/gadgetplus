from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

categories = Categories.objects.all()

# Create your views here.
def index(request):
    context = {
        'title': 'Gadget | Home',
        'categories': categories
    }

    return render(request, "main/index.html", context=context)


def contact(request):
    context = {
        'title': "Cadget | Contacts",
        'categories': categories
    }

    return render(request, "main/contact.html", context=context)