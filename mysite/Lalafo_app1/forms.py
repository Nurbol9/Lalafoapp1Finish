from .models import Product
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'price', 'phone_number',
                  'product_image', 'city', 'original', 'description']