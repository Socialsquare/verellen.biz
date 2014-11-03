from django.http import HttpResponse
from django.shortcuts import render

from verellen_web.models import Product

def index(request):
    products = Product.objects.all().order_by('price')
    return render(request, 'verellen_web/index.html', { 'products': products })
