from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from images.forms import CreateImageForm
from images.models import Image
from images.utils import setup_additional_image_fields


@login_required
def save_image(request):
    if request.POST:
        form = CreateImageForm(request.POST, request.FILES)
    else:
        form = CreateImageForm()

    if form.is_valid():
        setup_additional_image_fields(request, form.save(commit=False))
        messages.success(request, 'Image added successfully')
        return redirect('images:save_image')
    return render(request, 'images/save_image.html', {'form': form})


def image_detail(request, pk, slug):
    image = get_object_or_404(Image, pk=pk, slug=slug)
    return render(request, 'images/image_details.html', {'image': image})
