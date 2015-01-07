from django.http import Http404
from django.shortcuts import render

from products.models import Product, Category

def list(request, category_slug=None):
    category = Category.objects.filter(slug = category_slug).first()
    if category:
        products = Product.objects.filter(category = category)
    else:
        products = Product.objects.all()

    return render(request, 'products/list.html', { 'products': products, 'category': category })

def detail(request, product_id):
    try:
        product = Product.objects.get(pk = product_id)
    except Product.DoesNotExist:
        raise Http404

    images = product.image_set.all()

    col1_images = images[:2]
    col2_images = images[2:4]

    return render(request, 'products/detail.html', {
        'product': product,
        'col1_images': col1_images,
        'col2_images': col2_images
    })
