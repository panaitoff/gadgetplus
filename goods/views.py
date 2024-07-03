from django.shortcuts import render # type: ignore
from goods.models import Categories, Products

categories = Categories.objects.all()
products = Products.objects.all()



# Create your views here.
def categories(request):

    context = {
        'title': 'Gadget | Categories',
        'categories': categories,
        'products': products
    }

    return render(request, 'goods/categories.html', context=context)

def product(request):
    return render(request, 'goods/product.html')
