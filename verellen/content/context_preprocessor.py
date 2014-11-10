import models

from utils import get_content_model

def content(request):
    return { 'footer_content': get_content_model(models.FooterContent) }
