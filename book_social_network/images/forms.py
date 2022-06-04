from urllib import request

from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from images.models import Image


class CreateImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['url', 'title', 'description']
        widgets = {'url': forms.HiddenInput}
        error_messages = {
            'url': {'required': 'You must pass the url of the photo.'}
        }

    def clean_url(self):
        url: str = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        image_extension = url.rsplit('.', 1)[1]
        if image_extension not in valid_extensions:
            raise forms.ValidationError("The given url doesn't match valid image extensions.")
        return url

    def save(self, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title), image_url.rsplit('.', 1)[1].lower())
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()
        return image
