from django.shortcuts import render # type: ignore
from django.core.paginator import Paginator # type: ignore
from goods.models import Categories, Products


# Create your views here.
def categories(request, category_slug=None):
    
    if category_slug:
        products = Products.objects.filter(category__slug=category_slug)
    else:
        products = Products.objects.all()

    context = {
        'title': 'Gadget | Catalog',
        'products': products,
    }

    return render(request, 'goods/categories.html', context=context)

def phones_view(request, category):

    context = {
        'title': 'Gadget | Phones',
        'products': Products.objects.get(category=category)
    }

    return render(request, 'goods/categories.html', context=context)


def product(request, product_slug):

    prod = Products.objects.get(slug=product_slug) 

    context = {
        'title': 'Gadget | Categories',
        'product': prod
    }

    return render(request, 'goods/product.html', context=context)
