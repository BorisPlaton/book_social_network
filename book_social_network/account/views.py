from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def password_change_done(request):
    messages.success(request, "Your password has been successfully changed")
    return redirect('account:dashboard')


def password_reset_done(request):
    messages.info(request, "We've emailed you instructions for setting your password")
    return redirect('account:login')


def password_reset_complete(request):
    messages.success(request, "Password reset complete")
    return redirect('account:login')


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
