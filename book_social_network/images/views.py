from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404

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
@csrf_exempt
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if like_image(image_id, action, request.user):
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'failed'})


def image_detail(request, pk, slug):
    image = get_object_or_404(Image, pk=pk, slug=slug)
    return render(request, 'images/image_details.html', {'image': image})
