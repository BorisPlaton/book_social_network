from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404

from common.utils import get_paginator
from images.forms import CreateImageForm
from images.models import Image
from images.utils import setup_additional_image_fields, like_image


@login_required
def save_image(request):
    if request.POST:
        form = CreateImageForm(request.POST, request.FILES)
    else:
        form = CreateImageForm()

    if form.is_valid():
        setup_additional_image_fields(request.user, form.save(commit=False))
        messages.success(request, 'Image added successfully')
        return redirect('images:save_image')
    return render(request, 'images/save_image.html', {'form': form})


@login_required
@require_POST
@login_required
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if like_image(image_id, action, request.user):
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'failed'})


@login_required
def image_detail(request, pk, slug):
    image = get_object_or_404(Image, pk=pk, slug=slug)
    return render(request, 'images/image_details.html', {'image': image})


@login_required
def get_image_pagination(request):
    image_paginator = get_paginator(
        items_=Image.objects.filter(user=request.user),
        per_page=4,
        page=request.GET.get('page', 1),
    )
    return TemplateResponse(request, "includes/image_pagination.html", {"images": image_paginator})
