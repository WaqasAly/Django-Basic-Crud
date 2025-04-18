from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Product Name',
            'description': 'Product Description',
            'price': 'Product Price',
        }
        help_texts = {
            'name': 'Enter the name of the product.',
            'description': 'Enter a detailed description of the product.',
            'price': 'Enter the price of the product.',
        }
        error_messages = {
            'name': {
                'max_length': 'This name is too long.',
            },
            'price': {
                'invalid': 'Enter a valid price.',
            },
        }
        