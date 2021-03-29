from django import forms
from .models import Product

class NewProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["date_added","vendor"]
        widgets = {
            'description' : forms.Textarea(attrs={'cols': 60, 'rows': 6})
        }
