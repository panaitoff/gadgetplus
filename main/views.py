from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'title': 'Gadget',
    }

    return render(request, "main/index.html", context=context)


def about(request):
    return HttpResponse("<span>about</span>")