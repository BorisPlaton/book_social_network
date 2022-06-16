from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.decorators import unauthorized_required
from account.forms import UserRegistrationForm, ProfileEditForm, UserEditForm
from account.utils import create_user_and_profile
from common.utils import get_paginator
from images.models import Image


@login_required
def edit_profile(request):
    profile_form = ProfileEditForm(request.POST or None, instance=request.user.profile)
    user_form = UserEditForm(request.POST or None, instance=request.user)
    if request.POST:
        profile_form.files = request.FILES
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, "Changes were saved")
            return redirect('account:edit_profile')

    return render(request, 'account/edit_profile.html', {'profile_form': profile_form, 'user_form': user_form})


@login_required
def dashboard(request):
    image_paginator = get_paginator(
        items_=Image.objects.filter(user=request.user),
        per_page=5,
        page=request.GET.get('page', 1),
    )
    return (render(request, 'account/dashboard.html', {'image_paginator': image_paginator})
            if image_paginator
            else HttpResponse(image_paginator)
            )


@login_required
def password_change_done(request):
    messages.success(request, "Your password has been successfully changed")
    return redirect('account:dashboard')


@unauthorized_required
def registration(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        create_user_and_profile(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'],
        )
        return redirect('account:dashboard')
    return render(request, 'account/registration/registration.html', {'form': form})


@unauthorized_required
def password_reset_done(request):
    messages.info(request, "We've emailed you instructions for setting your password")
    return redirect('account:login')


@unauthorized_required
def password_reset_complete(request):
    messages.success(request, "Password reset complete")
    return redirect('account:login')
