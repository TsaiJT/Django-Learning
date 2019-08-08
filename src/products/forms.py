from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    title = forms.CharField(label = 'Title', 
                            widget = forms.TextInput(attrs={'placeholder':'Your title'}))
    description = forms.CharField()
    email = forms.EmailField()
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # Check the title information.
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'CFE' in title:
            raise forms.ValidationError('This is not a valid title1')
        return title


# Implement the raw form not from the ModelForm.
class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')
    #     if not 'CFE' in title:
    #         raise forms.ValidationError('This is not a valid title1')
    #     return title