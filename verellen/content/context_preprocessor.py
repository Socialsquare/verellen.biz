import models

from utils import get_content_model
from products.models import Category
from partner.utils import get_partner
from django.conf import settings

def content(request):
    product_categories = Category.objects.filter(product__isnull=False).distinct()

    partner = get_partner(request.user)
    hide_price = False
    hide_sales_tools = False
    if partner:
        hide_price = partner.hide_price
        hide_sales_tools = partner.hide_sales_tools

    return {
        'footer_content': get_content_model(models.FooterContent),
        'menu_content': get_content_model(models.MenuContent),
        'product_categories': product_categories,
        'hide_price': hide_price,
        'hide_sales_tools': hide_sales_tools,
    }

def google_analytics(request):
    """
    Use the variables returned in this function to
    render your Google Analytics tracking code template.
    """
    ga_prop_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', False)
    ga_domain = getattr(settings, 'GOOGLE_ANALYTICS_DOMAIN', False)
    if not settings.DEBUG and ga_prop_id and ga_domain:
        return {
            'GOOGLE_ANALYTICS_PROPERTY_ID': ga_prop_id,
            'GOOGLE_ANALYTICS_DOMAIN': ga_domain,
        }
    return {}
