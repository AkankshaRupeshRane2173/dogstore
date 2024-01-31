# forms.py

from django import forms
from .models import addnewpet

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = addnewpet
        fields = ['image']
