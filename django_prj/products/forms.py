from django import forms
from .models import Product

class NewProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["date_added","vendor"]
        widgets = {
            'description' : forms.Textarea(attrs={'class' : 'input-box2','style':'resize:none;'}),
            'name': forms.TextInput(attrs={"class":"input-box1"}),
            'price' : forms.NumberInput(attrs = {'input_type' :'numeric', 'class' : 'input-box3'}),
        }
