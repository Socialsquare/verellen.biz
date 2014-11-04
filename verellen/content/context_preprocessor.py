from content.models import FooterContent

def content(request):
    return { 'footer_content': FooterContent.objects.all()[0] }
