from django.http import HttpRequest

from images.models import Image


def setup_additional_image_fields(request: HttpRequest, image: Image):
    image.user = request.user
    image.save()
