from django.shortcuts import render

# Create your views here.
def categories(request):
    return render(request, 'goods/categories.html')

def product(request):
    return render(request, 'goods/product.html')