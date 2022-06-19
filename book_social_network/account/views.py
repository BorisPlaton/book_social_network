from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from account.decorators import unauthorized_required
from account.forms import UserRegistrationForm, ProfileEditForm, UserEditForm
from account.models import User
from account.utils import create_user_and_profile, subscribe_user
from actions.utils import get_followed_users_actions
from common.utils import get_paginator
from config import settings
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
    action_paginator = get_paginator(
        items_=get_followed_users_actions(request.user),
        per_page=settings.PAGINATION_PICTURES_AMOUNT,
        page=request.GET.get('page', 1),
    )
    return render(request, 'account/dashboard.html', {'actions': action_paginator})


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


def users_list(request):
    return render(request, 'account/users_list.html', {'users': User.objects.filter(is_active=True)})


def user_profile(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    images = get_paginator(
        items_=Image.objects.filter(user=user),
        per_page=settings.PAGINATION_PICTURES_AMOUNT,
        page=1,
    )
    return render(request, 'account/user_profile.html',
                  {
                      'current_user': user,
                      'images': images,
                      'is_following': request.user.is_following(user.pk)
                  })


@login_required
@require_POST
def follow(request):
    user_follower = request.user
    try:
        followed_user = User.objects.get(is_active=True, pk=request.POST.get('id'))
    except User.DoesNotExist:
        return JsonResponse({'status': 'fail', 'reason': 'Wrong user'})
    subscribe_user(user_follower, followed_user, True if request.POST.get('action').lower() == 'follow' else False)
    return JsonResponse({'status': 'success'})
