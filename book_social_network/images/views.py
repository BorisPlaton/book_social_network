from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from images.forms import CreateImageForm
from images.utils import setup_additional_image_fields


@login_required
def save_image(request):
    form = CreateImageForm(request.POST or None)
    if form.is_valid():
        setup_additional_image_fields(request, form.save(commit=False))
        messages.success(request, 'Image added successfully')
        return redirect('images:save_image')
    return render(request, 'images/save_image.html', {'form': form})

