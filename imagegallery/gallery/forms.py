from django import forms
from .models import MyImage

class ImageForm(forms.ModelForm):
    class Meta:
        model=MyImage
        fields=['image']