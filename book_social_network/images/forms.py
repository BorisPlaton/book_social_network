from django import forms

from images.models import Image


class CreateImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image', 'description']
