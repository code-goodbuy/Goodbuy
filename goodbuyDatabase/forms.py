from django import forms

from .models import Product


class AddNewProductForm(forms.ModelForm):
    code = forms.IntegerField(required=True)
    name = forms.CharField(required=True,strip=True)

    class Meta:
        model = Product
        fields = [
            "code",
            "name",
            "image",
            "brand",
            "corporation",
            "main_category",
            "sub_category",
        ]
