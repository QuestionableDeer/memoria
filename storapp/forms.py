from django import forms

class CodeUploadForm(forms.Form):
    name = forms.CharField(help_text='A brief name to help identify this code')
    code = forms.CharField(help_text='The code to be stored')
