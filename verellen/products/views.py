from django.http import Http404
from django.shortcuts import render

from products.models import Product, Category

from sorl.thumbnail import get_thumbnail

def list(request, category_slug=None):
    category = Category.objects.filter(slug = category_slug).first()
    if category:
        products = Product.objects.filter(category = category)
    else:
        products = Product.objects.all()

    return render(request, 'products/list.html', { 'products': products, 'category': category })

def home(request):
    categories = Category.objects.all()

    return render(request, 'products/home.html', { 'categories': categories })

def detail(request, product_id):
    try:
        product = Product.objects.get(pk = product_id)
    except Product.DoesNotExist:
        raise Http404

    images = product.image_set.all()

    main_image = images[0]
    col1_images = images[1:3]
    col2_images = images[3:6]

    return render(request, 'products/detail.html', {
        'product': product,
        'col1_images': col1_images,
        'col2_images': col2_images,
        'main_image': main_image
    })
