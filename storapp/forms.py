from django import forms

from decimal import Decimal

class CodeUploadForm(forms.Form):
    name = forms.CharField(help_text='A brief name to help identify this code')
    code = forms.CharField(help_text='The code to be stored')
    unlock_price = forms.DecimalField(min_value=Decimal(0.0), max_value=Decimal(99999.99), step_size=Decimal(0.01), decimal_places=2, help_text='Price in dollars to recover this code')

class ImageUploadForm(forms.Form):
    name = forms.CharField(help_text='A brief name to help identify this image')
    img = forms.ImageField(help_text='The image to be stored')
    unlock_price = forms.DecimalField(min_value=Decimal(0.0), max_value=Decimal(99999.99), step_size=Decimal(0.01), decimal_places=2, help_text='Price in dollars to recover this image')

