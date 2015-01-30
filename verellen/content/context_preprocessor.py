import models

from utils import get_content_model
from products.models import Category
from partner.utils import get_partner

def content(request):
    product_categories = Category.objects.filter(product__isnull=False).distinct()

    partner = get_partner(request.user)
    hide_price = False
    if partner:
        hide_price = partner.hide_price

    return {
        'footer_content': get_content_model(models.FooterContent),
        'menu_content': get_content_model(models.MenuContent),
        'product_categories': product_categories,
        'hide_price': hide_price,
    }
