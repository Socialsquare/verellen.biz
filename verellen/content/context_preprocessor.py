import models

from utils import get_content_model
from products.models import Category

def content(request):
    product_categories = Category.objects.all()
    return {
        'footer_content': get_content_model(models.FooterContent),
        'menu_content': get_content_model(models.MenuContent),
        'product_categories': product_categories,
    }
