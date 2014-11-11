from django.http import Http404
from django.shortcuts import render

from products.models import Product

def list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', { 'products': products })

def detail(request, product_id):
    try:
        product = Product.objects.get(pk = product_id)
    except Product.DoesNotExist:
        raise Http404

    return render(request, 'products/detail.html', { 'product': product })
