from django import forms
from products.models import Product, Image

class ProductAdminForm(forms.ModelForm):
    main_image = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super(ProductAdminForm, self).__init__(*args, **kwargs)
        self.fields['main_image'].queryset = Image.objects.filter(product=self.instance)

    class Meta:
        model = Product
