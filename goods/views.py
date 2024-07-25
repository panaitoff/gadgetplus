from django.shortcuts import render # type: ignore
from django.core.paginator import Paginator # type: ignore
from goods.models import Categories, Products
from goods.utils import q_search

# Create your views here.
def categories(request, category_slug=None):
    
    page = request.GET.get('page', 1)
    filtr = request.GET.get('filter', None)
    query = request.GET.get('q', None)

    if category_slug is not None:
        products = Products.objects.filter(category__slug=category_slug)
    elif query:
        products = q_search(query)
    else:
        products = Products.objects.all()

    if filtr:
        products = products.order_by(filtr)

    paginator = Paginator(products, 4)
    current_page = paginator.page(page)

    context = {
        'title': 'Gadget | Catalog',
        'products': current_page,
        'category_slug': category_slug,
        'filter': filtr,
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
